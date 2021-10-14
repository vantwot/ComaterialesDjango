from django.urls import path, include

from comaterialesApp import views

urlpatterns = [
    path('latest-products/', views.LatestProductslis.as_view())
]