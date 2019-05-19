from django import forms

from .models import Money

# フォームのクラスを作成する
class SpendingForm(forms.Form):
    #　各フォームの性質を定義。フィールド定義とラベル付けを行う
    choices = (
            ('家賃','家賃'),
            ('通信費','通信費'),
            ('保険費','保険費'),
            ('クレカ','クレカ'),
            ('ガソリン代','ガソリン代'),
            ('雑費','雑費'),
            ('光熱費','光熱費'),
            ('車代','車代'),
            ('奨学金','奨学金'),
            ('ローン','ローン'),
            ('食費','食費'),
            ('交遊費','交遊費'),
            ('NHK受信料','NHK受信料'),
            ('その他','その他'),
            )
    amount = forms.IntegerField(label='金額')
    exchange_date = forms.DateTimeField(
            label='日付',
            required=True,
            widget=forms.DateInput(attrs={"type":"date"}),
            input_formats=['%Y-%m-%d']
            )
    detail = forms.CharField(
            max_length = 200,
            label='用途'
            )
    category = forms.ChoiceField(choices=choices,label='カテゴリー')
