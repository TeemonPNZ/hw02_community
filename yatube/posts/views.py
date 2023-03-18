from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POST_NUM = 10


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:POST_NUM]
    context = {'title': title,
               'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_NUM]
    context = {
        'group': group,
        'posts': posts,
        'slug': slug,
        'title': 'Лев Толстой – зеркало русской революции.'
    }
    return render(request, template, context)
