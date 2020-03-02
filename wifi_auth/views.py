from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, DetailView
from .models import Router
from .mikrotik_api import RouterOSData, Mysql_connect
import requests
import pymysql
import os
from django.views import generic
import json


def get_info(request):
    name = request.POST['name']
    second = request.POST['second']
    context = {'name': name, 'second': second}
    return HttpResponse('your name is {} and your second is {}'.format(name, second))


def index(request):
    routers = Router.objects.all()
    context = {'routers': routers, }

    return render(request, 'wifi_auth/router_list.html', context)


class RouterDetailView(DetailView):
    model = Router


def get_active_users(request, pk):
    router = Router.objects.get(pk=pk)
    get_data = RouterOSData(router.ip_address, router.admin_login, router.admin_password)
    return HttpResponse(get_data.get_active_users())


def get_cookie(request, pk):
    router = Router.objects.get(pk=pk)
    get_data = RouterOSData(router.ip_address, router.admin_login, router.admin_password)
    return HttpResponse(get_data.get_cookies())


def get_all_users(request):
    mysql_connect = Mysql_connect("185.41.121.156", "xmahopsc", "yvxn6akk", "radius")
    users_from_base = mysql_connect.get_users_from_base()
    router = Router.objects.get(id=2)
    router.available = False
    router.save()
    return HttpResponse(users_from_base)


def get_smsru_balance(request):
    r = requests.get("https://sms.ru/my/balance?api_id=20A92FF0-8FBC-BCE0-DE99-FF7AA5FFF3C8&json=1")
    return HttpResponse(r)