from django.contrib import admin

from .models import Event, UsLocation, Notes

admin.site.register(Event)
admin.site.register(UsLocation)
admin.site.register(Notes)
