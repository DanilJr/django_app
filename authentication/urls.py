from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('<int:id>/', views.user_view_id, name='user_view_id')
    ]