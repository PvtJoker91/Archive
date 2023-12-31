# Generated by Django 4.2.2 on 2023-07-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Договор', 'verbose_name_plural': 'Договоры'},
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Client', to='ad.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='Номер договора'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ad.product', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заключения'),
        ),
    ]
