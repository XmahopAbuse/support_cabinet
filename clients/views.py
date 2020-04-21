from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NewClient
from django.utils import timezone
from .filters import NewClientFilter


def index(request):
    clients = NewClient.objects.all()
    filter = NewClientFilter(request.GET,queryset=clients)
    context = {'clients':clients,
               'filter':filter}
    return render(request,'clients/newclient_list.html',context)

