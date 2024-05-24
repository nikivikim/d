# Generated by Django 5.0.6 on 2024-05-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_balance_unique_together_balance_date2_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='balance',
            unique_together={('user', 'date')},
        ),
        migrations.AddField(
            model_name='indicatorvalue',
            name='period_year',
            field=models.IntegerField(default=1, verbose_name='Год периода'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='balance',
            name='date',
            field=models.DateTimeField(verbose_name='Период'),
        ),
        migrations.RemoveField(
            model_name='balance',
            name='date2',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='date3',
        ),
    ]