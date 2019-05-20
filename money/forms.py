from django import forms
from .models import Money


class SpendingForm(forms.ModelForm):
    exchange_date = forms.DateTimeField(
        label='日付',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )
    # https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/#overriding-the-default-fields

    class Meta:
        model = Money
        fields = ['amount', 'exchange_date', 'detail', 'category']
