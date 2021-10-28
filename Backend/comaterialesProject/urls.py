"""comaterialesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from comaterialesApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from comaterialesApp.views.userCreateView import UserCreateView
from comaterialesApp.views.productCreateView import productos
from comaterialesApp.views.categoriaView import categorias
from comaterialesApp.views.familiasView import familias
from comaterialesApp.views.productCreateView import productoDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    # funcionalidad del simplejwt
    path('refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('productos/', views.productos.as_view()),
    path('categorias/', views.categorias.as_view()),
    path('familia/', views.familias.as_view()),
    path('productos/<int:pk>/', views.productoDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)