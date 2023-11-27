import csv
import pytest

from unittest.mock import patch
from app.documents.models import Transaction

@pytest.mark.parametrize('test_data, expected', [[1, 1/23, -5], [2, 1/24, -23.9], [3, 1/25, 51]])
@patch("app.documents.utils.process_transactions")
def test_process_documents(test_data, mocked_process_function):
    mocked_process_function(test_data)

    transactions = Transaction.objects.all()

    assert transactions.count() == 3


@pytest.mark.parametrize('test_data, expected', [[1, 1/23, -5, 0], [2, 1/24, -23.9, 0], [3, 1/25, 51, 0]])
@patch("app.documents.utils.process_transactions")
def test_process_documents_more_than_three_nodes(test_data, mocked_process_function):
    mocked_process_function(test_data)

    transactions = Transaction.objects.all()

    assert transactions.count() == 0


@pytest.mark.parametrize('test_data, expected', [[1, 1/23], [2], [3, 1/25]])
@patch("app.documents.utils.process_transactions")
def test_process_documents_less_than_three_nodes(test_data, mocked_process_function):
    mocked_process_function(test_data)

    transactions = Transaction.objects.all()

    assert transactions.count() == 0
