from django.contrib import admin
from .models import event, booking
from django.contrib.admin.actions import delete_selected as django_delete_selected
# Register your models here.

@admin.register(event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','date','start_time','seats','booked_seats','price',)
    list_filter = ("date", "category")
    fields = ( 'name', 'category','date','start_time','end_time','description','seats','booked_seats','price','image_tag', )
    readonly_fields = ('image_tag',)

@admin.register(booking)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','mobile','event')
    list_filter = ('event__name',"email", "mobile")