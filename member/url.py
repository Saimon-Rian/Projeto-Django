from django.urls import path
from .views import create_user, user_profile, edit_profile, setting_profile, create_profile, PasswordChange
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('create_profile/', create_profile, name='create_profile'),
    path('<int:user_id>/user_page/', user_profile, name='user_profile'),
    path('<int:user_id>/edit_profile', edit_profile, name='edit_profile'),
    path('user_page/<int:id>/settings_profile', setting_profile, name='setting_profile'),
    path('user_page/password/', PasswordChange.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),
]
