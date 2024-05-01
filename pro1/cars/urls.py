from django.urls import path
from cars.views import get_info

urlpatterns = [
    path('', get_info)
]