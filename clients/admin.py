from django.contrib import admin
from .models import NewClient
from django.db import models

@admin.register(NewClient)
class NewClientAdmin(admin.ModelAdmin):
   # fields = ('city', 'name', 'phone','message','manager','status')

    fieldsets = (
        (None, {
            'fields': ('city', 'name', 'phone','message','manager','status'),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_send',),
        }),
    )


    list_display = ('id','name', 'phone', 'manager','status')
    list_filter = ('city','status')
    search_fields = ['name']
    view_on_site = False
