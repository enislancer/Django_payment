# accounts/urls.py
from django.urls import path

from . import views
from . import views_stripe
from . import views_paypal
app_name = 'payment'
urlpatterns = [
    path('success', views.payment_success, name='success'),
    path('cancel', views.payment_cancel, name='cancel'),
    path('select-gateway', views.select_gateway, name='select_gateway'),

    # ----- Paypal ----------
    path('paypal/checkout', views_paypal.checkout, name='paypal_checkout'),

    # ----- Stripe ----------
    path('stripe/checkout', views_stripe.checkout, name='stripe_checkout'),
]