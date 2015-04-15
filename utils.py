from .settings import PRODUCT_NAME
from .models import Transaction, PAYMENT_STATUS


def get_plan_price_details(request):
    detail = {}
    try:
        from accounts.models import Plan
        plan = Plan.objects.get(id=int(request.GET.get('plan')))
        detail['price'] = plan.price
        detail['currency'] = plan.currency
        detail['plan_id'] = plan.id

    except Exception as e:
        print(e)
        detail['price'] = 60
        detail['currency'] = 'usd'
        detail['plan_id'] = 2
    return detail


def get_product_details(request):
    product = {}
    try:
        from accounts.models import Plan
        plan = Plan.objects.get(id=int(request.GET.get('plan')))
        product['name'] = 'Plan "{}" for {}'.format(plan.name, PRODUCT_NAME)
    except:
        product['name'] = 'Business user for {}'.format(PRODUCT_NAME)
    return product


def create_transaction(request, plan_id, currency, amount, payment_gateway, status=PAYMENT_STATUS[0][0]):
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="payment_transaction")
    plan = models.PositiveIntegerField()
    currency = models.CharField(max_length=5, null=True, blank=True)
    payment_gateway = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=PAYMENT_STATUS, null=True, blank=True)
    """
    print("create_transaction", PAYMENT_STATUS[0][0])
    instance = Transaction.objects.create(user=request.user, plan=plan_id, currency=currency,
                                          payment_gateway=payment_gateway, amount=amount,
                                          status=PAYMENT_STATUS[0][0])
    return instance.id


def update_transaction(request, status):
    transaction_id = request.GET.get('transaction_id')
    instance = None
    if transaction_id:
        instance = Transaction.objects.get(id=transaction_id)
        if instance.status == PAYMENT_STATUS[0][0]:
            instance.status = status
            try:
                from accounts.models import Plan
                print(instance.plan)
                if status == PAYMENT_STATUS[1][0]:
                    request.user.user_plan.plan = Plan.objects.get(id=instance.plan)
                    request.user.user_plan.total_amount += instance.amount
                    request.user.user_plan.save()
            except Exception as e:
                print(e)
            instance.save()
    return instance
