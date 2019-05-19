from django.db import models

"""
Djangoのモデルは、Modelクラスの継承クラスとして定義される
"""


# Create your models here.
class Money(models.Model):
    # お金をやり取りした日付、収支の内訳、金額を定義
    exchange_date = models.DateTimeField('日付')
    detail = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.detail + '￥' + str(self.amount)


"""
return文で返された値は、管理者ページでMoneysのレコードにアクセスしたときに表示される
"""