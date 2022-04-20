from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_word, name='hello'),
    path('book/', views.book_all, name='book_all'),
    path('book/<int:id>/', views.book_detail, name='book_detail')
]
