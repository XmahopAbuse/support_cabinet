import django_filters
from django import forms
from .models import NewClient


class NewClientFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder':'Населенный пункт'}))
    class Meta:
        model = NewClient
        fields = ['name','city']