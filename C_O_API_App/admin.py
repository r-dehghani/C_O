from django.contrib import admin
from .models import indexes , trigger

class AdminMode(admin.ModelAdmin):
    list_display = ["symbolisin", "yesterday_variation", "asking_price" , "biding_price" ,"opening_price"]
    search_fields = ["symbolisin"]

admin.site.register(indexes , AdminMode)


class AdminMode1(admin.ModelAdmin):
    list_display = ["user_symbol", "oper", "desired_price", "right_operand" , "is_fired"]
    search_fields = ["user_symbol"]

admin.site.register(trigger , AdminMode1)