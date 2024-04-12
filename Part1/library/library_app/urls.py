from django.urls import path

from library_app import views


urlpatterns = [
    path('api/checkout/', views.checkout),
    path('api/return/', views.return_book),
    path('api/fulfill/', views.fulfill),
]
