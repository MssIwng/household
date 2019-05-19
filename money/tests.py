import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import resolve

from money.models import Money
from money.views import index


class TestURL(TestCase):
    def test_URL_reslove(self):
        url = resolve('/money/')
        self.assertEqual(url.func, index)

        url = resolve('/money/2019/05')
        self.assertEqual(url.func, index)


class TestMoneyModel(TestCase):
    def test_db_is_empty(self):
        money = Money.objects.all()
        self.assertEqual(money.count(), 0)

    def test_save_data(self):
        exchange_date = timezone.now()
        detail = "テスト"
        amount = 100
        category = "食費"

        Money.objects.create(
            exchange_date = exchange_date,
            detail = detail,
            amount = amount,
            category = category,
            )
        obj = Money.objects.all()
        self.assertEqual(obj.count(),1)
        self.assertEqual(obj[0].exchange_date, exchange_date)
        self.assertEqual(obj[0].detail, detail)
        self.assertEqual(obj[0].amount, amount)
        self.assertEqual(obj[0].category, category)
