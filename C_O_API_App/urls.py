from django.urls import path
from .views import Indexes_list , Index_info


urlpatterns = [
    path('', Indexes_list.as_view()),
    path('<slug:symbolISIN>/', Index_info.as_view())

]
