# Generated by Django 4.2.2 on 2023-07-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_alter_product_options_alter_client_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='second_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='third_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
