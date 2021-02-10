from django.shortcuts import render, redirect
from .models import Order

# Create your views here.


def order_list(request):
    context = {'order_list': Order.get_all()}
    return render(request, 'order_list.html', context)

def order_delete(request, id):
    Order.delete_by_id(id)
    return redirect('/order/')

def order_view_id(request, id):
    context = {'order_id': Order.get_by_id(id)}
    return render(request, 'order_id.html', context)