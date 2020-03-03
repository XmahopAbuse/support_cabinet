from django.contrib import admin
from django.urls import path
from . import views
from .views import RouterDetailView

urlpatterns = [
    path('testhttp/',views.get_info),
    path('',views.index),
    path('router/<int:pk>/', RouterDetailView.as_view(), name='router-detail'),
    path('router/<int:pk>/active', views.get_active_users, name='active_users'),
    path('router/<int:pk>/cookie', views.get_cookie, name="cookies"),
    path('all_users/',views.get_all_users, name="all_users"),
    path('smsru_balance/',views.get_smsru_balance)
    # path('router/<int:pk>/ping', views.do_ping, name="doping")
]
