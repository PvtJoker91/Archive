from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='home'),
    path('search/', search_page, name='search'),
    path('search/search_results/', SearchResultsView.as_view(), name='search_results'),
    path('contract/<int:contract_pk>', ContractDetail.as_view(), name='contract_detail'),
    path('logistic/', logistic_page, name='logistic'),
    path('registration/', registration_page, name='registration'),
    path('requests/', requests_page, name='requests'),
]
