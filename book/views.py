from django.shortcuts import render, redirect
from .models import Book



def books_list(request):
    context = {}
    context['books_list'] = Book.get_all()
    return render(request, 'books_list.html', context)



def books_view_id(request, id):
    context = {}
    context['book_id'] = Book.get_by_id(id)
    return render(request, 'books_id.html', context)



def books_delete(request, id):
    Book.delete_by_id(id)
    return redirect('/books/')
