from django.db import models

"""
Djangoのモデルは、Modelクラスの継承クラスとして定義される
"""
SELECT_CHOICES = (
    ('家賃', '家賃'),
    ('通信費', '通信費'),
    ('保険費', '保険費'),
    ('クレカ', 'クレカ'),
    ('ガソリン代', 'ガソリン代'),
    ('雑費', '雑費'),
    ('光熱費', '光熱費'),
    ('車代', '車代'),
    ('奨学金', '奨学金'),
    ('ローン', 'ローン'),
    ('食費', '食費'),
    ('交遊費', '交遊費'),
    ('NHK受信料', 'NHK受信料'),
    ('その他', 'その他'),
)


# Create your models here.
class Money(models.Model):
    # お金をやり取りした日付、収支の内訳、金額を定義
    exchange_date = models.DateTimeField('日付')
    detail = models.CharField('用途', max_length=200)
    amount = models.IntegerField('金額', default=0)
    category = models.CharField('カテゴリー', max_length=10, choices=SELECT_CHOICES)

    def __str__(self):
        return self.detail + '￥' + str(self.amount)


"""
return文で返された値は、管理者ページでMoneysのレコードにアクセスしたときに表示される
"""