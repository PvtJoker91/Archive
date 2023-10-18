from django.contrib import admin
from ad.models import *


class ContractAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'contract_number', 'time_create')



admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Contract, ContractAdmin)

