from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    #path('',ClientsListView.as_view(), name='clients_list'),
    path('', views.index,name="clients_index")
]
