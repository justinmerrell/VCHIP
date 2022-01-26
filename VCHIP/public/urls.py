''' vchip.app URL locations '''

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
	path('', views.scanner, name='Scanner'),
	path('link/', views.GenerateLink, name='Link'),
	path('<code>/', views.code, name='Coded'),
]
