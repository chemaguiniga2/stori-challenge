from datetime import datetime
from decimal import Decimal

from app.documents.models import Account, Transaction
from app.documents.enum import TransactionType


def process_transactions(info):
    total_balance = 0
    debit_amount = 0
    credit_amount = 0

    debit_transactions = 0
    credit_transactions = 0
    extra_data = {}
    type = ""

    for transaction in info:
        if (
            len(transaction) < 3
            or len(transaction) > 3
        ):
            raise Exception("Format not allowed")


        total_balance += transaction[2]

        if transaction[2] > 0:
            credit_amount += transaction[2]
            credit_transactions += 1
            type = TransactionType.CREDIT
        else:
            debit_amount += transaction[2]
            debit_transactions += 1
            type = TransactionType.DEBIT

        date = transaction[1].split('/')
        transaction_date = datetime(datetime.now().year, int(date[0]), int(date[1]))

        extra_data = process_transaction_date(transaction_date, extra_data)

        Transaction.objects.update_or_create(
            created=transaction_date,
            amount=Decimal(transaction[2]),
            type=type
        )


    per_month = []
    for i in extra_data:
        per_month.append(f"{i}: {extra_data[i]}")
        
    res = {
        "total_balance": total_balance,
        "debit_amount": debit_amount,
        "credit_amount": credit_amount,
        "debit_avg_amount": debit_amount/debit_transactions,
        "credit_avg_amount": credit_amount/credit_transactions,
        "per_month": per_month
    }

    account = Account.objects.get(id=1)
    account.average_debit_amount = Decimal(f"{debit_amount/debit_transactions}")
    account.average_credit_amount = Decimal(f"{credit_amount/credit_transactions}")
    account.total_balance = Decimal(f"{total_balance}")
    account.save()

    return res


def process_transaction_date(transaction_date, extra_data):
    month = transaction_date.strftime("%b")
    if month in extra_data:
        extra_data[month] += 1
    else:
        extra_data.update({
            month: 1
        })

    return extra_data
