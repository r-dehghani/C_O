from django.urls import path
from .views import indexes_list , index_info , browse_symbol


urlpatterns = [
    path('list/', indexes_list.as_view()),
    path('<slug:symbolisin>/', index_info.as_view()),
    path('browse_symbol/insert/', browse_symbol.as_view()),

]
