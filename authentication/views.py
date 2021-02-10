from django.shortcuts import render, redirect
from .models import CustomUser

# Create your views here.

def user_list(request):
    context = {'user_list': CustomUser.get_all()}
    return render(request, 'user_list.html', context)

def user_delete(request, id):
    CustomUser.delete_by_id(id)
    return redirect('/authentication/')

def user_view_id(request, id):
    context = {'user_id': CustomUser.get_by_id(id)}
    return render(request, 'user_id.html', context)
