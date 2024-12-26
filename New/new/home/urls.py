from django.contrib import admin
from django.urls import path
from . import views


# Django admin customizations
admin.site.site_header = "Welcome to Gowtham's Admin portal"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title = "Welcome to the Admin Dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.handle_query, name='query'),
    path('book/', views.book, name='book'),
    path('base/', views.base, name='base'),
    path('base/booking.html/', views.book, name='book'),
    path('base/query.html', views.handle_query, name='query'),
    path('base.html', views.base, name='base'),
    path('booking.html', views.book, name='book'),
    path('query.html', views.handle_query, name='query'),
    path('venues.html', views.venues, name='venues'),
    path('venues/', views.venues, name='venues'),
    

    ]
