from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index, name='dhcp_info_index'),
    path('add/',views.add_switch,name="dhcp_info_add_switch")
]
