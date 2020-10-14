from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:pk>/', views.details, name='details'),
    path('purchase/<int:pk>/', views.purchase, name='purchase'),
    path('my_puchases/', views.my_purchases, name='my-purchases'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)