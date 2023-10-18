from django.db.models import Q, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from .utils import *
from .forms import *


def index_page(request):
    menu = [
        {'title': 'Поиск', 'url_name': 'search'},
        {'title': 'Регистрация документов', 'url_name': 'registration'},
        {'title': 'Логистика', 'url_name': 'logistic'},
        {'title': 'Запросы', 'url_name': 'requests'},
    ]
    context = {
        'menu': menu,
        'title': 'Добро пожаловать в архив!'
    }
    return render(request, 'ad/index.html', context=context)


def search_page(request):
    # Поиск через формы Django, а не HTML. Пока ХЗ как...
    # second_name = ''
    # name = ''
    # third_name = ''
    # passport = ''
    # form = SearchForm(request.GET)
    # if form.is_valid():
    #     second_name = form.cleaned_data.get("second_name")
    #     name = form.cleaned_data.get("name")
    #     third_name = form.cleaned_data.get("third_name")
    #     passport = form.cleaned_data.get("passport")
    # context = {'form': form, 'second_name': second_name,
    #            'name': name, 'third_name': third_name,
    #            'passport': passport, 'title': 'Поиск клиентов'}
    context = {'title': 'Поиск клиентов'}
    return render(request, 'ad/search.html', context)


class SearchResultsView(ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = 'ad/search_results.html'

    def get_queryset(self):
        second_name = self.request.GET.get('q').strip()
        name = self.request.GET.get('n').strip()
        third_name = self.request.GET.get('o').strip()
        passport = self.request.GET.get('p').strip()
        contract = self.request.GET.get('c').strip()
        if second_name or name or third_name or passport or contract:
            # client_list = Client.objects.filter(second_name__icontains=second_name,
            #                                     name__icontains=name,
            #                                     third_name__icontains=third_name,
            #                                     passport__icontains=passport,
            #                                     contracts__contract_number__icontains=contract
            #                                     ).prefetch_related('contracts').distinct()
            client_list = Client.objects.filter(second_name__icontains=second_name,
                                                name__icontains=name,
                                                third_name__icontains=third_name,
                                                passport__icontains=passport,
                                                contracts__contract_number__icontains=contract
                                                ).prefetch_related(Prefetch('contracts', queryset=Contract.objects.select_related('product'))).distinct()
        else:
            client_list = None
        return client_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результаты поиска'
        return context


class ContractDetail(DetailView):
    model = Contract
    template_name = 'ad/contract_detail.html'
    pk_url_kwarg = 'contract_pk'
    context_object_name = 'contract_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр договора'
        return context


def logistic_page(request):
    return HttpResponse('Логистика')


def requests_page(request):
    return HttpResponse('Запросы')


def registration_page(request):
    return HttpResponse('Регистрация документов')
