from django.db import models
from django.urls import reverse

class Client(models.Model):
    second_name = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    third_name = models.CharField(max_length=30, verbose_name='Отчество')
    passport = models.IntegerField(verbose_name='Номер паспорта')
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.second_name} {self.name} {self.third_name}'
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    def get_absolute_url(self):
        return reverse('client', kwargs={'client_pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название продукта')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    def __str__(self):
        return self.name


class Contract(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='contracts', verbose_name='Договор')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='contracts', verbose_name='Клиент')
    contract_number = models.IntegerField(unique=True, max_length=10, verbose_name='Номер договора')
    barcode = models.IntegerField(unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата заключения')
    is_registred = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return self.product.name


    def get_absolute_url(self):
        return reverse('contract_detail', kwargs={'contract_pk':self.pk})
