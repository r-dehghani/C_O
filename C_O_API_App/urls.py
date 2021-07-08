from django.urls import path
from .views import indexes_list , index_info


urlpatterns = [
    path('', indexes_list.as_view()),
    path('<slug:symbolisin>/', index_info.as_view())

]
