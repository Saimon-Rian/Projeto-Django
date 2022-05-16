import django_filters
from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm


# Create your views here.
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    post_list = None
    # import ipdb; ipdb.set_trace()
    if request.GET.get('author', None):
        post_list = Post.objects.filter(author__username__icontains=request.GET.get('author'))

    if request.GET.get('categories', None):
        post_list = Post.objects.filter(category__category_name__iexact=request.GET.get('categories'))

    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')

    # if start_date and end_date:
    #    posts = posts.filter(
    #        post_date__range=[start_date, end_date]
    #    )

    if request.POST.get('start_date'):
        posts = posts.filter(
                post_date__gte=request.POST.get('start_date')
            )

    if request.POST.get('end_date'):
        posts = posts.filter(
                post_date__lte=request.POST.get('end_date')
            )

    data = {
        'filters': {'author_username': request.GET.get('author'), 'category_name': request.GET.get('categories')},
        'post_list': post_list,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'home.html', data)


def detail_post_view(request, id):
    post = Post.objects.get(id=id)

    data = {
        'post': post,
    }
    return render(request, 'post_detail.html', data)


def add_post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            return redirect('home')
    data = {
        'form': form
    }
    return render(request, 'post_add.html', data)


def edit_post_view(request, id):
    post = Post.objects.get(id=id)
    form = EditForm(instance=post)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=id)
    data = {
        'post': post,
        'form': form
    }
    return render(request, 'post_edit.html', data)


def delete_post_view(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')


def message(request, id):
    post = Post.objects.get(id=id)
    data = {
        'post': post
    }
    return render(request, 'post_delete.html', data)


def add_category_view(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.user)
        if form.is_valid():
            category = form.save(commit=False)
            category.creator_id = request.user.id
            category.save()
            return redirect('category_add')
    data = {
        'form': form
    }
    return render(request, 'category_add.html', data)


def list_category_view(request):
    categories = Category.objects.filter(creator_id=request.user)
    # categories = Category.objects.all()

    data = {
        'categories': categories
    }
    return render(request, 'category_list.html', data)


def delete_category_view(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_list')


def category_message(request, id):
    category = Category.objects.get(id=id)
    data = {
        'category': category
    }
    return render(request, 'category_delete.html', data)


def category_view(request, cat):
    categories_posts = Post.objects.filter(category__category_name=cat)
    data = {'cat': cat.title(),
            'categories_posts': categories_posts}
    return render(request, 'categories.html', data)
