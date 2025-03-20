from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('search/', views.search, name='search')
]
