from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import  forms
from django import forms
from .models import Indicator, Balance, IndicatorValue
from users.models import Indicator, Balance, IndicatorValue

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'username':'Имя пользователя (логин)',
            'first_name': 'Имя',
            'password1': 'Имя пользователя (логин)',
            'first_name': 'Имя',
        }


class BalanceForm(forms.ModelForm):
    date = forms.DateTimeField(label='Период', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Balance
        fields = ['date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        indicators = Indicator.objects.all()
        for indicator in indicators:
            self.fields[f'indicator_{indicator.code}'] = forms.FloatField(
                label=indicator.name,
                required=True
            )
        self.user = user

    def save(self, commit=True):
        balance = super().save(commit=False)
        balance.user = self.user
        if commit:
            balance.save()
            indicators = Indicator.objects.all()
            for indicator in indicators:
                value = self.cleaned_data[f'indicator_{indicator.code}']
                IndicatorValue.objects.create(balance=balance, indicator=indicator, value=value)
        return balance