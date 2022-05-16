from django.urls import path
from .views import home, detail_post_view, edit_post_view, delete_post_view, message, add_post_view, add_category_view, \
   list_category_view, delete_category_view, category_message, category_view


urlpatterns = [
   path('', home, name='home'),
   path('add_post/', add_post_view, name='post_add'),
   path('post/<int:id>', detail_post_view, name='post_detail'),
   path('post_update/<int:id>', edit_post_view, name='post_edit'),
   path('post_confirm/<int:id>', message, name='confirm'),
   path('post_delete/<int:id>', delete_post_view, name='post_delete'),
   path('categories/<str:cat>', category_view, name='categories'),
   path('category_list/', list_category_view, name='category_list'),
   path('add_category/', add_category_view, name='category_add'),
   path('category_delete/<int:id>', delete_category_view, name='category_delete'),
   path('category_confirm/<int:id>', category_message, name='category_confirm'),
]
