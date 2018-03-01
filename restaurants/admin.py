from django.contrib import admin

from .models import Restaurant, Item, Rfavorite, Ifavorite

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Rfavorite)
admin.site.register(Ifavorite)