# Generated by Django 4.2.4 on 2023-11-24 02:16

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "average_debit_amount",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.0"), max_digits=12
                    ),
                ),
                (
                    "average_credit_amount",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.0"), max_digits=12
                    ),
                ),
                (
                    "total_balance",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.0"), max_digits=12
                    ),
                ),
            ],
            options={
                "verbose_name": "Account",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.0"), max_digits=12
                    ),
                ),
                ("type", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
            },
        ),
    ]
