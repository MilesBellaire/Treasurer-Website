from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name="title"),
    path('current-requests/', views.current_requests, name="current_requests"),
    path('request/', views.request, name="request"),
    path('spreadsheet/', views.spreadsheet, name="spreadsheet"),
]