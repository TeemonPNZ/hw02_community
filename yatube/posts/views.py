from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'title': title,
               'text': 'Главная страница',
               'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'slug': slug,
        'text': 'Лев Толстой – зеркало русской революции.'
    }
    return render(request, template, context)
