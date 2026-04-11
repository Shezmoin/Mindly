from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
import stripe

from users.models import UserProfile

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

    GET: Displays donation form with preset amounts (£5/10/25/50) and custom option
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
                messages.error(request, 'Donation amount must be at least £1.')
                return render(request, 'payments/donate.html')

            messages.info(request, f'Stripe integration pending. Would process £{amount:.2f} donation.')
            return redirect('payments:index')

        except (ValueError, KeyError):
            messages.error(request, 'Invalid donation amount. Please try again.')
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
    success_url = request.build_absolute_uri(reverse('payments:success'))
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
        messages.error(request, 'Unable to start checkout right now. Please try again.')
        return redirect('payments:pricing')


def success_view(request):
    """
    Payment success confirmation page.
    Displayed after successful Stripe checkout (donation or subscription).
    """
    return render(request, 'payments/success.html')


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
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
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
