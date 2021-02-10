from django.urls import path
from . import views


urlpatterns = [
    path('', views.books_list, name = 'main'),
    path('<int:id>',views.books_view_id , name = "book"),
    path('delete/<int:id>',views.books_delete , name = 'book_delete'),
    # path('',views. , name = ),
]