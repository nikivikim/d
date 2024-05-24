from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Indicator(models.Model):
    name = models.CharField('Название кода', max_length=100)
    code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Период')

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        unique_together = ('user', 'date')

class IndicatorValue(models.Model):
    balance = models.ForeignKey(Balance, related_name='indicator_values', on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    value = models.FloatField('Значение')

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'