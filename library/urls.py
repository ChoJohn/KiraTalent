from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getBooks, name="get_books"),
    path('api/<str:book_id>/', views.updateBook, name="update_book")
]