from django.contrib import admin
from .models import indexes

class AdminMode(admin.ModelAdmin):
    list_display = ["symbolisin", "variation", "top" , "bottom" ,"opening_price"]
    search_fields = ["symbolisin"]

admin.site.register(indexes , AdminMode)