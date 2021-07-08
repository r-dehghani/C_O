from django.contrib import admin
from .models import Indexes

class AdminMode(admin.ModelAdmin):
    list_display = ["symbolISIN", "variation", "top" , "bottom" ,"opening_price"]
    search_fields = ["symbolISIN"]

admin.site.register(Indexes , AdminMode)