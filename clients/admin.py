from django.contrib import admin
from .models import NewClient, District
from django.db import models

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(NewClient)
class NewClientAdmin(admin.ModelAdmin):
   # fields = ('city', 'name', 'phone','message','manager','status')

    fieldsets = (
        (None, {
            'fields': ('city', 'name', 'phone','message','manager','status','ticket_from','district','comment'),
        }),
        ('dont change it', {
            'classes': ('collapse',),
            'fields': ('is_send','message_id','reply_id'),
        }),
    )


    list_display = ('id','name','city','phone', 'status', 'manager','ticket_from','district','comment','created')
    list_filter = ('city','status')
    search_fields = ['name']
    view_on_site = False
