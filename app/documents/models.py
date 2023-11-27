from decimal import Decimal
from django.db import models


class Transaction(models.Model):
    """
    A model that represents the transaction that is storaged
    in the csv file.
    """
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.0")
    )
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Account(models.Model):
    """
    A model that represents the account information.
    """
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    average_debit_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.0")
    )
    average_credit_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.0")
    )
    total_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.0")
    )

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
