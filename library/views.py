from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.
# @api_view(["GET"])
# def books(request):
#     bookList = "hello world"

#     return Response(bookList)

@api_view(["GET"])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)