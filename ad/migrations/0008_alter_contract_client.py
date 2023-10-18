# Generated by Django 4.2.2 on 2023-07-22 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0007_alter_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='ad.client', verbose_name='Клиент'),
        ),
    ]
