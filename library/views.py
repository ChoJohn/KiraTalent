from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.
@api_view(["GET"])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT"])
def updateBook(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(instance=book, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)