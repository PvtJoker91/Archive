# Generated by Django 4.2.2 on 2023-07-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0008_alter_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_number',
            field=models.IntegerField(max_length=10, unique=True, verbose_name='Номер договора'),
        ),
    ]
