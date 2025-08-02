from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='table'),
    path('single', views.single, name='single')
]
