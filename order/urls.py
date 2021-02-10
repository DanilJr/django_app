from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('delete/<int:id>/', views.order_delete, name='order_delete'),
    path('<int:id>/', views.order_view_id, name='order_view_id')
    ]