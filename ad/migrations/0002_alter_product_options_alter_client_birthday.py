# Generated by Django 4.2.2 on 2023-07-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(),
        ),
    ]
