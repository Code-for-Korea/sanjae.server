from django.urls import path
from . import views

app_name = "case_app"

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:ruling_id>/', views.detail, name='detail'),
    path('<int:ruling_id>/edit/', views.edit, name='edit'),
    path('<int:ruling_id>/submit/', views.submit, name='submit'),
]