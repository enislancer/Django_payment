from django.shortcuts import render

# Create your views here.
from . import settings
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.decorators import login_required
from .utils import update_transaction
from .models import PAYMENT_STATUS


@login_required
def select_gateway(request):
    plan = request.GET.get('plan')
    return render(request, 'payment/select_gateway.html', {'plan': plan})


@login_required
def payment_success(request):
    update_transaction(request, status=PAYMENT_STATUS[1][0])
    return render(request, '{}/success.html'.format(settings.APP_NAME))


@login_required
def payment_cancel(request):
    update_transaction(request, status=PAYMENT_STATUS[3][0])
    return render(request, '{}/cancel.html'.format(settings.APP_NAME))
