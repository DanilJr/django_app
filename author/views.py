from django.shortcuts import render, redirect
from .models import Author

def authors_list(request):
    context = {}
    context['authors_list'] = Author.get_all()
    return render(request, 'authors_list.html', context)

def view_author_id(request, id):
    context = {}
    context['author_by_id'] = Author.get_by_id(id)
    return render(request, 'author_by_id.html', context)



def delete_author_by_id(request, id):
    Author.delete_by_id(id)
    return redirect('/authors/')
# Create your views here.
