from django.contrib import admin
from django.urls import path, include

app_name = 'kontas'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('transacoes.urls')),
]
