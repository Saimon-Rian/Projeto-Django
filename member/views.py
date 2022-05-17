from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse, reverse_lazy

from .forms import SignUpForm, ProfilePageForm, EditProfileForm,UserForm, CreateProfileForm, PasswordsChangingForm
from website.models import UserProfile


def create_user(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    data = {
        'form': form
    }
    return render(request, 'registration/register.html', data)


def create_profile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user.id
            profile.save()
            return redirect('user_page')
    data = {
        'form': form,
    }
    return render(request, 'registration/create_profile_page.html', data)


def user_profile(request, user_id):
    profile = UserProfile.objects.get(user_id=user_id)
    form = ProfilePageForm
    data = {
        'form': form,
        'profile': profile
    }
    return render(request, 'registration/user_profile.html', data)


def edit_profile(request, user_id):
    profile = UserProfile.objects.get(user_id=user_id)
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=user_id)
    data = {
        'profile': profile,
        'form': form
    }
    return render(request, 'registration/edit_user_profile.html', data)


def setting_profile(request, id):
    # import ipdb; ipdb.set_trace()
    user = User.objects.get(id=id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', id)
    data = {
        'user': user,
        'form': form
    }
    return render(request, 'registration/profile_settings.html', data)


class PasswordChange(PasswordChangeView):
    from_class = PasswordsChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
