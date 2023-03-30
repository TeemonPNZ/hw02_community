from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from django.core.paginator import Paginator


NUM_POSTS = 10


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    post_list = Post.objects.all()
    paginator = Paginator(post_list, NUM_POSTS) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': title
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    post_list = group.posts.all()
    paginator = Paginator(post_list, NUM_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template, context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    template = 'posts/profile.html'
    username = get_object_or_404(User, username=username)
    all_author_posts = username.posts.all()
    posts_count = all_author_posts.count()

    paginator = Paginator(all_author_posts, NUM_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = (f'Профиль пользователя {username}')
    context = {
        'username': username,
        'posts_count': posts_count,
        'all_posts': all_author_posts,
        'page_obj': page_obj,
        'title': title
    }
    return render(request, title, template, context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, id=post_id)
    posts_count = Post.objects.filter(author_id=post.author_id).count()
    group = Group.objects.get(id=post.group_id)
    author = User.objects.get(id=post.author_id)
    template = 'posts/post_detail.html'
    title = post.text[0:30]
    context = {
        'post': post,
        'posts_count': posts_count,
        'group': group,
        'author': author,
        'title': title
    }
    return render(request, title, template, context)
 