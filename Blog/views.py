from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from datetime import date


# Create your views here.

def indexView(request):
    # blogs = Post.objects.filter(category='blogs')
    # case_studies = Post.objects.filter(category='case_studies')
    context = {
        # 'blogs': blogs.order_by('date')[:4],
        # 'case_studies': case_studies.order_by('date')[:4],
    }
    return render(request, 'blog/index.html', context)


def adminView(request):
    return render(request, 'blog/admin.html')


# these 3 functions for single post
def blogsView(request, name):
    # posts = Post.objects.all()
    # post = Post.objects.get(post_url=name)

    context = {
        # 'post': post, 'category': 'blogs',
        # 'related_posts': posts.order_by('date')[:3]
    }
    return render(request, 'blog/post.html', context)


def case_studiesView(request, name):
    # posts = Post.objects.all()
    # post = Post.objects.get(post_url=name)
    context = {
        # 'post': post, 'category': 'case_studies',
        # 'related_posts': posts.order_by('date')[:3]
    }
    return render(request, 'blog/post.html', context)


def podcastView(request, name):
    # posts = Post.objects.all()
    # post = Post.objects.get(post_url=name)
    context = {
        # 'post': post, 'category': 'case_studies',
        # 'related_posts': posts.order_by('date')[:3]
    }
    return render(request, 'blog/podcast.html', context)


# for specific category
def categoryView(request, name):
    if '/' in name:
        name = name.rpartition('/')[0]

    if name == 'blogs':
        template_name = 'blog/blogs.html'
    elif name == 'podcast':
        template_name = 'blog/podcast.html'
    elif name == 'case_studies':
        template_name = 'blog/case_studies.html'
    else:
        template_name = 'blog/index.html'

    # posts = Post.objects.filter(category=name)

    context = {
        # 'important_posts': posts.order_by('-date'),
        # 'recent_posts': posts
    }

    return render(request, template_name, context)


def category_detailView(request, name1, name2):
    if '/' in name1:
        name1 = name1.rpartition('/')[0]
    if name1 == 'blogs':
        template_name = 'blog/blogs.html'
    else:
        template_name = 'blog/case_studies.html'

    # posts = Post.objects.filter(category=name1, sub_category=name2)

    context = {
        # 'important_posts': posts.order_by('date'),
        # 'recent_posts': posts
    }
    return render(request, template_name, context)


def filter_post_keywordView(request, type, keyword):
    data = {}
    # posts = Post.objects.filter(category=type).filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword))
    # data = serializers.serialize('json', posts)
    return JsonResponse(data, safe=False)


def filter_post_dateView(request, type, range):
    today = date.today()
    posts = {}
    # if range == 'week':
    #     posts = Post.objects.filter(category=type).filter(date__week=today.isocalendar()[1])
    # elif range == 'month':
    #     posts = Post.objects.filter(category=type).filter(date__month=today.month)
    # else:
    #     posts = Post.objects.filter(category=type).filter(date__year=today.year)

    data = serializers.serialize('json', posts)
    return JsonResponse(data, safe=False)
