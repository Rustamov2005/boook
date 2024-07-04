from django.shortcuts import render
from .models import Book


def home(request):
    return render(request, 'home.html')


def books(request):
    if request.method == 'POST':
       search = request.POST['search']
       all_books = Book.objects.filter(title__icontains=search)
       if books:
            return render(request, 'books.html', {'books': all_books, "value": search, "message": "Books not found"})
       else:
           return render(request, 'books.html', {'message': "Not fount"})
    all_books = Book.objects.all()
    return render(request, 'books.html', {'books': all_books})



