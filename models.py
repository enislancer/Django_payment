from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

PAYMENT_STATUS = (
    ('initiated', 'Initiated'),
    ('success', 'Success'),
    ('failed', 'failed'),
    ('cancelled', 'cancelled')
)


class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="payment_transaction")
    plan = models.PositiveIntegerField()
    currency = models.CharField(max_length=5, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_gateway = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=30, choices=PAYMENT_STATUS, null=True, blank=True)

    def __str__(self):
        return "{} - {}({}) {} - {}".format(self.user, self.amount, self.currency, self.payment_gateway, self.status)