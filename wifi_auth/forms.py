from django.forms import ModelForm
from .models import Router
from django import forms
from django.core.exceptions import ValidationError

class RouterForm(ModelForm):
    router_name = forms.CharField(label="Название", widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputRouterName',
        'placeholder':'Pp-',

    }),
                                  error_messages={'invalid': 'your custom error message'}
                                  )
    ip_address = forms.CharField(label="IP-адрес", widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputRouterIP',
        'placeholder':'IP',
        'data-parsley-type':'digits',
    }))
    admin_login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputRouterAdminLogin',
        'placeholder':'Admin login'
    }))
    admin_password = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputRouterAdminPassword',
        'placeholder':'Admin password'
    }))

    class Meta:
        model = Router
        fields = ['router_name','ip_address','admin_login','admin_password']