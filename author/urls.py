from django.urls import path
from . import views


urlpatterns = [
    path('', views.authors_list, name = 'author_main'),
    path('<int:id>', views.view_author_id , name ='author_by_id'),
    path('delete/<int:id>', views.delete_author_by_id, name ='delete_author_by_id'),
]
 