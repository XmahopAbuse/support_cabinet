from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('login/',views.user_login, name='login'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="change_password"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('pass_change/', views.change_password, name="pass_change"),
]
