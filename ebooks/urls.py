from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.add_book, name='add_book'),
    path('success/', lambda request: render(request, 'success.html'), name='book_success'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('update/<int:book_id>/', views.update_book, name='update_book'),
]