from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from website.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')
        labels = {
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PasswordsChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        labels = {
            'bio': 'Bio',
            'profile_picture': 'Foto de perfil',
            'social_medias': 'Redes sociais'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sobre mim'}),
            'profile_picture': forms.FileInput(),
            'social_medias': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Redes sociais'}),
        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture', 'social_medias')
        labels = {
            'bio': 'Bio',
            'profile_picture': 'Foto de perfil',
            'social_media': 'Redes sociais'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sobre mim'}),
            'profile_picture': forms.FileInput(),
            'social_medias': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Redes sociais'}),
        }


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture', 'social_medias')
        labels = {
            'bio': 'Bio',
            'profile_picture': 'Foto de perfil',
            'social_media': 'Redes sociais'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sobre mim'}),
            'profile_picture': forms.FileInput(),
            'social_medias': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Redes sociais'}),
        }