import stripe

from django.shortcuts import render, reverse

# Create your views here.
from . import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .utils import *


from .settings import STRIPE_SECRETE_KEY
stripe.api_key = STRIPE_SECRETE_KEY


def create_checkout_session_util(amount, currency, transaction_id):
    cancel_url = settings.CANCEL_URL + str(transaction_id)
    success_url = settings.SUCCESS_URL + str(transaction_id)
    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - lets capture the payment later
        # [customer_email] - lets you prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancel_url,
            # billing_address_collection="required",
            # shipping_address_collection={'allowed_countries':['US', 'CA']},
            payment_method_types=["card"],
            line_items=[
                {
                    "name": PRODUCT_NAME,
                    "quantity": 1,
                    "currency": currency,
                    "amount": amount * 100,
                    "description": _("payment for {}".format(PRODUCT_NAME))
                }
            ]
        )
        return checkout_session['id']
    except Exception as e:
        print(e)
        return ""


@login_required
def checkout(request):
    product = get_product_details(request)
    plan = get_plan_price_details(request)
    price = plan['price']
    currency = plan['currency']
    plan_id = plan['plan_id']
    transaction_id = create_transaction(request, plan_id, currency, amount=price, payment_gateway=settings.STRIPE)
    session_id = create_checkout_session_util(int(price), currency, transaction_id)
    return render(request, 'payment/stripe/checkout.html', {'PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
                                                            'product_name': product['name'],
                                                            'currency': currency, 'price': price,
                                                            "session_id": session_id})
