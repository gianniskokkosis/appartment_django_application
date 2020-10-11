from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:pk>', views.details, name='details'),
    path('purchase/<int:pk>', views.purchase, name='purchase'),
]
