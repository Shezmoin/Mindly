from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
import json
import logging
import stripe

from users.models import UserProfile

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY


def index_view(request):
    """
    Main payments support page showing both donation and subscription options.

    Displays:
    - One-time donation options (£5, £10, £25, custom)
    - Premium subscription at £9.99/month
    - FAQ section
    """
    return render(request, 'payments/index.html')


def pricing_view(request):
    """
    Pricing page showing Free and Premium plans.
    """
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'payments/pricing.html', context)


def donate_view(request):
    """
    Donation form page for one-time payments in GBP.

    GET: Displays donation form with preset amounts (£5/10/25/50)
    and custom option
    POST: Processes donation and redirects to Stripe checkout
    """
    if request.method == 'POST':
        try:
            # Get donation amount from form
            amount_choice = request.POST.get('amount')
            custom_amount = request.POST.get('custom_amount')

            # Determine final amount
            if amount_choice == 'custom':
                amount = float(custom_amount)
            else:
                amount = float(amount_choice)

            # Validate amount
            if amount < 1:
                messages.error(
                    request,
                    'Donation amount must be at least £1.',
                )
                return render(request, 'payments/donate.html')

            # Stripe expects amount in pence (GBP)
            stripe_amount = int(amount * 100)

            # Create Stripe Checkout session for one-time payment
            success_url = request.build_absolute_uri(reverse('payments:success')) + '?type=donation'
            cancel_url = request.build_absolute_uri(reverse('payments:cancel'))

            session_kwargs = {
                'payment_method_types': ['card'],
                'mode': 'payment',
                'line_items': [
                    {
                        'price_data': {
                            'currency': 'gbp',
                            'product_data': {
                                'name': 'Mindly Donation',
                            },
                            'unit_amount': stripe_amount,
                        },
                        'quantity': 1,
                    }
                ],
                'success_url': success_url,
                'cancel_url': cancel_url,
            }

            if request.user.is_authenticated and request.user.email:
                session_kwargs['customer_email'] = request.user.email

            session = stripe.checkout.Session.create(**session_kwargs)
            return HttpResponseRedirect(session.url)

        except (ValueError, KeyError):
            messages.error(
                request,
                'Invalid donation amount. Please try again.',
            )
            return render(request, 'payments/donate.html')
        except Exception as e:
            logger.error(f"Stripe error: {e}")
            messages.error(
                request,
                'Unable to start donation checkout. Please try again later.',
            )
            return render(request, 'payments/donate.html')

    return render(request, 'payments/donate.html')


def subscribe_view(request):
    """
    Legacy subscription endpoint.
    Redirects to pricing on GET and to checkout on POST.
    """
    if request.method == 'POST':
        return redirect('payments:checkout')
    return redirect('payments:pricing')


@login_required
def checkout_view(request):
    """
    Create Stripe Checkout Session for premium subscription and redirect.
    """
    success_url = request.build_absolute_uri(reverse('payments:success')) + '?type=subscription'
    cancel_url = request.build_absolute_uri(reverse('payments:cancel'))

    session_kwargs = {
        'mode': 'subscription',
        'line_items': [
            {
                'price': settings.STRIPE_PRICE_ID,
                'quantity': 1,
            }
        ],
        'success_url': success_url,
        'cancel_url': cancel_url,
    }

    if request.user.email:
        session_kwargs['customer_email'] = request.user.email

    try:
        session = stripe.checkout.Session.create(**session_kwargs)
        return HttpResponseRedirect(session.url)
    except Exception:
        messages.error(
            request,
            'Unable to start checkout right now. Please try again.',
        )
        return redirect('payments:pricing')


def success_view(request):
    """
    Payment success confirmation page.
    Displayed after successful Stripe checkout (donation or subscription).
    """
    payment_type = request.GET.get('type', '')
    return render(request, 'payments/success.html', {'payment_type': payment_type})


def cancel_view(request):
    """
    Payment cancellation page.
    Displayed when user cancels Stripe checkout.
    """
    return render(request, 'payments/cancel.html')


@csrf_exempt
@require_POST
def webhook_view(request):
    """
    Stripe webhook endpoint.

    Verifies Stripe signature and upgrades users to premium after
    checkout.session.completed events.
    """
    payload = request.body
    sig_header = (request.META.get('HTTP_STRIPE_SIGNATURE', '') or '').strip()
    endpoint_secret = (settings.STRIPE_WEBHOOK_SECRET or '').strip()

    if not sig_header or not endpoint_secret:
        return HttpResponse(status=400)

    try:
        event = stripe.Webhook.construct_event(
            payload.decode('utf-8'),
            sig_header,
            endpoint_secret,
        )

        # Only upgrade to premium if the session is a subscription
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            mode = session.get('mode')
            customer_email = session.get('customer_email')
            if mode == 'subscription' and customer_email:
                User = get_user_model()
                try:
                    user = User.objects.get(email=customer_email)
                    profile, _ = UserProfile.objects.get_or_create(user=user)
                    profile.subscription_tier = 'premium'
                    profile.save()
                except User.DoesNotExist:
                    logger.warning(f"No user found for email {customer_email}")
            elif mode == 'payment':
                # Optionally, record the donation here (future enhancement)
                logger.info(f"Donation received from {customer_email}")
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.warning('Invalid signature: %s', e)
        # Local-dev fallback: allow Stripe CLI forwarded events in DEBUG mode.
        if not settings.DEBUG:
            return HttpResponse(status=400)
        try:
            event = json.loads(payload.decode('utf-8'))
        except (ValueError, TypeError):
            return HttpResponse(status=400)

    if event.get('type') == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_email')

        if customer_email:
            User = get_user_model()
            user = User.objects.filter(email=customer_email).first()
            if user:
                profile, _ = UserProfile.objects.get_or_create(user=user)
                profile.subscription_tier = 'premium'
                profile.save(update_fields=['subscription_tier'])

    return HttpResponse(status=200)
