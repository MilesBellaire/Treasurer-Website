from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name="title"),
    path('current-requests/', views.current_requests, name="current_requests"),
    path('request/', views.request, name="request"),
    path('budget_tracking/', views.budget_tracking, name="budget_tracking"),
    path('spreadsheet/', views.spreadsheet, name="spreadsheet"),
    path('track/', views.tracking, name="tracking"),
    path('pivot_table/', views.pivot_table, name="pivot_table"),
    path('index/', views.index, name="index"),
]