from django.shortcuts import render

# Create your views here.
from . import settings
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from .utils import *
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    plan = get_plan_price_details(request)
    price = plan['price']
    currency = plan['currency']
    plan_id = plan['plan_id']
    transaction_id = create_transaction(request, plan_id, currency, amount=price, payment_gateway=settings.PAYPAL)
    return render(request, 'payment/paypal/checkout.html', {'currency': currency.upper(), 'price': price,
                                                            'paypal_client_id': settings.PAYPAL_CLIENT_ID,
                                                            'success_url': settings.SUCCESS_URL + str(transaction_id)})
