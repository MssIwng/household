from django import forms
from .models import Money


class SpendingForm(forms.ModelForm):
    exchange_date = forms.DateTimeField(
        label='日付',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']  #日時関連のフィールドを扱う際に利用するバリデーション
    )
    # https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/#overriding-the-default-fields

    class Meta:
        model = Money
        fields = ['amount', 'exchange_date', 'detail', 'category']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

class CheckForm(forms.Form):
    str = forms.CharField(label='String')

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError(' You input "NO"! ')


