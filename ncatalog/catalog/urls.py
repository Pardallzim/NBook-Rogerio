from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('like/<int:books_id>/', like_books, name='like_books'),
    path('comment/<int:books_id>/', comment_books, name='comment_books'),
    path('add/', add_books, name='add_books'),
    path('edit/<int:books_id>/', edit_books, name='edit_books'),
    path('delete/<int:books_id>/', delete_books, name='delete_books'),
    path('detail/<int:books_id>/', detail_books, name='detail_books'),
]