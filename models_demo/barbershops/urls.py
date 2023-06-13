from django.urls import path

from models_demo.barbershops.views import index

urlpatterns = [
    path('', index, name='index')
]