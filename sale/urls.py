from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sale import views
from .views import *
app_name = 'sale'
urlpatterns = [
    path('',views.index, name='index'),
    path('list',views.list, name='list'),
    path('detail/<int:pk>', views.detail, name = 'detail'),

    path('list2/', SaleListView.as_view(), name = 'ListView'),
    path('detail2/<int:pk>', SaleDetailView.as_view(), name = 'DetailView')
]