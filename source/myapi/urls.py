from django.urls import path
from .views import add_view, divide_view, multiply_view, subtract_view


app_name = 'myapi'


urlpatterns = [
    path('add/', add_view, name='add')
]