from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from users.forms import UserCreationForm
from users.models import Indicator, IndicatorValue
from django.http import JsonResponse
from django.shortcuts import render
from .models import Balance
from .forms import BalanceForm
import pandas as pd
import matplotlib.pyplot as plt
# users/views.py

from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.http import JsonResponse
from .models import Balance, Indicator, IndicatorValue
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Balance, Indicator, IndicatorValue
from .forms import BalanceForm
import matplotlib.pyplot as plt
import io
import urllib, base64
import io
import base64
import urllib
import numpy as np
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LinearRegression
from .models import Balance
import matplotlib.pyplot as plt

@login_required
def create_balance(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST, user=request.user)
        if form.is_valid():
            balance = form.save()
            return redirect('report', balance_id=balance.id)
    else:
        form = BalanceForm(user=request.user)
    return render(request, 'balance_form.html', {'form': form})

import io
import base64
import urllib
import numpy as np
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LinearRegression
from .models import Balance, Indicator, IndicatorValue
import matplotlib.pyplot as plt


@login_required
def report(request, balance_id):
    balance = get_object_or_404(Balance, id=balance_id, user=request.user)
    indicator_values = balance.indicator_values.all()

    # Найдем значения необходимых индикаторов
    indicator_1200 = next((iv.value for iv in indicator_values if iv.indicator.code == '1200'), 0)
    indicator_1500 = next((iv.value for iv in indicator_values if iv.indicator.code == '1500'), 0)
    indicator_cash = next((iv.value for iv in indicator_values if iv.indicator.code == '1100'), 0)
    indicator_quick_assets = next((iv.value for iv in indicator_values if iv.indicator.code == '1400'), 0)
    total_assets = sum(iv.value for iv in indicator_values if iv.indicator.code.startswith('TA'))
    equity = sum(iv.value for iv in indicator_values if iv.indicator.code.startswith('EQ'))
    inventory = next((iv.value for iv in indicator_values if iv.indicator.code == '1300'), 0)  # Example for inventory
    receivables = next((iv.value for iv in indicator_values if iv.indicator.code == '1400'),
                       0)  # Example for receivables

    # Вычисляем коэффициенты ликвидности
    current_ratio = indicator_1200 / indicator_1500 if indicator_1500 != 0 else 0
    quick_ratio = (indicator_quick_assets + indicator_cash) / indicator_1500 if indicator_1500 != 0 else 0
    absolute_ratio = indicator_cash / indicator_1500 if indicator_1500 != 0 else 0
    autonomy_ratio = equity / total_assets if total_assets != 0 else 0

    # Анализ эффективности управления запасами и дебиторской задолженностью (простые примеры)
    inventory_turnover = total_assets / inventory if inventory != 0 else 0
    receivables_turnover = total_assets / receivables if receivables != 0 else 0

    # Генерация графика с помощью matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Данные для гистограммы
    labels = ['Текущая ликвидность', 'Быстрая ликвидность', 'Абсолютная ликвидность']
    values = [current_ratio, quick_ratio, absolute_ratio]

    ax.bar(labels, values)
    ax.set_title('Коэффициенты ликвидности')
    ax.set_ylabel('Значение')

    # Преобразование графика в изображение PNG
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    # Прогнозирование с использованием линейной регрессии
    # Допустим, у нас есть прошлые данные по доходам и расходам
    past_data = {
        'revenues': [100, 150, 200, 250, 300],  # Примерные данные
        'expenses': [80, 120, 160, 200, 240],  # Примерные данные
    }
    future_periods = 5  # Количество будущих периодов для прогноза

    # Прогнозирование доходов
    X = np.arange(len(past_data['revenues'])).reshape(-1, 1)
    y = np.array(past_data['revenues'])
    model = LinearRegression().fit(X, y)
    future_X = np.arange(len(past_data['revenues']), len(past_data['revenues']) + future_periods).reshape(-1, 1)
    future_revenues = model.predict(future_X)

    # Прогнозирование расходов
    y = np.array(past_data['expenses'])
    model = LinearRegression().fit(X, y)
    future_expenses = model.predict(future_X)

    # Прогнозирование прибыли
    future_profits = future_revenues - future_expenses

    # Рекомендации на основе значений коэффициентов
    recommendations = []
    if current_ratio < 1:
        recommendations.append("Увеличьте текущие активы или уменьшите текущие обязательства.")
    else:
        recommendations.append("Коэффициент текущей ликвидности в норме.")

    if quick_ratio < 1:
        recommendations.append("Увеличьте ликвидные активы или уменьшите текущие обязательства.")
    else:
        recommendations.append("Коэффициент быстрой ликвидности в норме.")

    if absolute_ratio < 0.5:
        recommendations.append("Увеличьте денежные средства для повышения абсолютной ликвидности.")
    else:
        recommendations.append("Коэффициент абсолютной ликвидности в норме.")

    if autonomy_ratio < 0.4:
        recommendations.append("Увеличьте собственный капитал для снижения финансового риска.")
    else:
        recommendations.append("Коэффициент автономии в норме.")

    return render(request, 'report.html', {
        'balance': balance,
        'current_ratio': current_ratio,
        'quick_ratio': quick_ratio,
        'absolute_ratio': absolute_ratio,
        'autonomy_ratio': autonomy_ratio,
        'inventory_turnover': inventory_turnover,
        'receivables_turnover': receivables_turnover,
        'chart': uri,
        'recommendations': recommendations,
        'future_revenues': future_revenues,
        'future_expenses': future_expenses,
        'future_profits': future_profits,
        'indicator_1200': indicator_1200,
        'indicator_1500': indicator_1500,
        'indicator_cash': indicator_cash,
        'indicator_quick_assets': indicator_quick_assets,
        'inventory': inventory,
        'receivables': receivables,
        'equity': equity,
        'total_assets': total_assets,
    })
def balance_form(request):
    # Handle form submission or rendering
    pass

def liquidity(request):
    form = BalanceForm()
    data = {
        'form': form
    }
    return render(request, 'liquidity_calculator.html', data)



@login_required
def profile(request):
    balances = Balance.objects.filter(user=request.user).prefetch_related('indicator_values__indicator').order_by('-date')
    return render(request, 'profile.html', {'balances': balances})


def your_view(request):
    form = BalanceForm()
    data = {
        'form': form
    }
    return render(request, 'liquidity_calculator.html', data)

    #indicators = Indicator.objects.all()
    #return render(request, 'liquidity_calculator.html', {'indicators': indicators})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

