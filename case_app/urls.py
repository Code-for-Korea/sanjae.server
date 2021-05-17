from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:ruling_id>/', views.detail, name='detail'),
]