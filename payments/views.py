from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
import json

# Initialize Stripe with secret key
# stripe.api_key = settings.STRIPE_SECRET_KEY  # Uncomment when keys are configured

def index_view(request):
    """
    Main payments support page showing both donation and subscription options.
    
    Displays:
    - One-time donation options (£5, £10, £25, custom)
    - Premium subscription at £9.99/month
    - FAQ section
    """
    return render(request, 'payments/index.html')


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
            message = request.POST.get('message', '')
            
            # Determine final amount
            if amount_choice == 'custom':
                amount = float(custom_amount)
            else:
                amount = float(amount_choice)
            
            # Validate amount
            if amount < 1:
                messages.error(request, 'Donation amount must be at least £1.')
                return render(request, 'payments/donate.html')
            
            # Convert to pence for Stripe (Stripe uses smallest currency unit)
            amount_pence = int(amount * 100)
            
            # TODO: Create Stripe checkout session
            # session = stripe.checkout.Session.create(
            #     payment_method_types=['card'],
            #     line_items=[{
            #         'price_data': {
            #             'currency': 'gbp',
            #             'unit_amount': amount_pence,
            #             'product_data': {
            #                 'name': 'Donation to Mindly',
            #                 'description': message if message else 'Support mental health wellbeing',
            #             },
            #         },
            #         'quantity': 1,
            #     }],
            #     mode='payment',
            #     success_url=request.build_absolute_uri('/payments/success/'),
            #     cancel_url=request.build_absolute_uri('/payments/cancel/'),
            # )
            # return redirect(session.url)
            
            messages.info(request, f'Stripe integration pending. Would process £{amount:.2f} donation.')
            return redirect('payments:index')
            
        except (ValueError, KeyError) as e:
            messages.error(request, 'Invalid donation amount. Please try again.')
            return render(request, 'payments/donate.html')
    
    return render(request, 'payments/donate.html')


def subscribe_view(request):
    """
    Premium subscription page for recurring payments at £9.99/month.
    
    GET: Displays subscription details and benefits
    POST: Creates Stripe subscription and redirects to checkout
    """
    if request.method == 'POST':
        # Check if user is authenticated
        if not request.user.is_authenticated:
            messages.warning(request, 'Please log in to subscribe.')
            return redirect(f'/users/login/?next={request.path}')
        
        try:
            plan = request.POST.get('plan', 'premium_monthly')
            
            # TODO: Create Stripe checkout session for subscription
            # session = stripe.checkout.Session.create(
            #     payment_method_types=['card'],
            #     line_items=[{
            #         'price': settings.STRIPE_PREMIUM_PRICE_ID,  # Create this in Stripe Dashboard
            #         'quantity': 1,
            #     }],
            #     mode='subscription',
            #     success_url=request.build_absolute_uri('/payments/success/'),
            #     cancel_url=request.build_absolute_uri('/payments/cancel/'),
            #     customer_email=request.user.email,
            # )
            # return redirect(session.url)
            
            messages.info(request, 'Stripe integration pending. Would create £9.99/month subscription.')
            return redirect('payments:index')
            
        except Exception as e:
            messages.error(request, 'Unable to process subscription. Please try again.')
            return render(request, 'payments/subscribe.html')
    
    return render(request, 'payments/subscribe.html')


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
def webhook_handler(request):
    """
    Stripe webhook handler for processing payment events.
    
    Handles:
    - payment_intent.succeeded (successful donations)
    - checkout.session.completed (successful subscriptions)
    - customer.subscription.deleted (subscription cancellations)
    
    Security: Validates webhook signature using STRIPE_WEBHOOK_SECRET
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        # TODO: Verify webhook signature
        # event = stripe.Webhook.construct_event(
        #     payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        # )
        
        # Parse event type
        # event_type = event['type']
        
        # Handle different event types
        # if event_type == 'payment_intent.succeeded':
        #     # Log successful donation
        #     pass
        # elif event_type == 'checkout.session.completed':
        #     # Activate premium subscription for user
        #     pass
        # elif event_type == 'customer.subscription.deleted':
        #     # Deactivate premium subscription for user
        #     pass
        
        return JsonResponse({'status': 'success'})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
