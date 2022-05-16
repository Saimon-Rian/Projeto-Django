from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="user_profile", unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/profile_pictures/')
    social_medias = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
