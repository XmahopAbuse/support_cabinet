from django.shortcuts import render

def index(request):
    return render(request,'dhcp_info/index.html')

def add_switch(request):
    return render (request,'dhcp_info/add.html')