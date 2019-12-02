from django.urls import path
from .views import add_view, divide_view, multiply_view, subtract_view


app_name = 'myapi'


urlpatterns = [
    path('add/', add_view, name='add'),
    path('divide/', divide_view, name='divide'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply')
]