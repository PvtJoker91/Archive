from django.db.models import Count
from .models import *

menu = [{'title': 'Поиск документов', 'url_name': 'search'},
        {'title': 'Регистрация документов', 'url_name': 'registration'},
        {'title': 'Логистика', 'url_name': 'logistic'},
        {'title': 'Запросы', 'url_name': 'requests'},
        {'title': 'Все клиенты', 'url_name': 'clients'}, ]

class DataMixin:
    paginate_by = 20
    user_menu = menu.copy()
    def get_user_context(self, **kwargs):
        context = kwargs
#        context['menu'] = user_menu
        return context