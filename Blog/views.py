from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from datetime import date
from Blog import models, forms
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def permission_check(user):
    return user.is_staff or user.is_superuser and user.is_active


def indexView(request):
    blogs = models.Post.objects.filter(category=1) # Need to Update Later
    case_studies = models.Post.objects.filter(category=1) # Need to Update Later
    categories = models.BlogCategory.objects.all()
    subcategories = models.BlogSubCategory.objects.all()

    context = {
        'blogs': blogs.order_by('date')[:4],
        'case_studies': case_studies.order_by('date')[:4],
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'blog/index.html', context)


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminView(request):
    form = forms.PostForm()
    tag_list = models.Tags.objects.all()
    subCategory = ''
    filterOption = ''
    subcat = ''
    subfil = ''
    # print(request.POST)
    if request.method == 'POST':
        inputItems = request.POST
        category = request.POST.get('category')
        tags = request.POST.getlist('tagName')
        tag_lists = []
        for t in tag_list:
            tag_lists.append(str(t))
        # check = all(item in tag_lists for item in tags)
        for item in tags:
            for existing_item in tag_lists:
                if item != existing_item:
                    # new_tag = models.Tags.objects.create(tag=item)
                    print(item)
                else:
                    tag_lists.remove(existing_item)
                    tags.remove(item)
                    break
        # print(tag_lists)
        # print(tags)
        # print(check)
        for i in inputItems:
            if i == "subCategory":
                subCategory = request.POST.get('subCategory')
            if i == "filterOption":
                filterOption = request.POST.get('filterOption')

        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            cat = models.BlogCategory.objects.get(pk=category)
            if subCategory:
                subcat = models.BlogSubCategory.objects.get(pk=subCategory)
            if filterOption:
                subfil = models.FilterOption.objects.get(pk=filterOption)
            post = form.save(commit=False)
            post.author = request.user
            post.category = cat
            if subcat:
                post.sub_categories = subcat
            if subfil:
                post.filter_option = subfil
            # post.save()
            return HttpResponseRedirect(reverse('blog_app:index'))

    context = {
        'form': form,
        'tag_list': tag_list,
    }
    return render(request, 'blog/admin.html', context)


# these 3 functions for single post
def blogsView(request, name):
    posts = models.Post.objects.all()
    post = models.Post.objects.get(post_url=name)

    context = {
        'post': post, 'category': 'blogs',
        'related_posts': posts.order_by('date')[:3]
    }
    return render(request, 'blog/post.html', context)


def case_studiesView(request, name):
    posts = models.Post.objects.all()
    post = models.Post.objects.get(post_url=name)

    context = {
        'post': post, 'category': 'case_studies',
        'related_posts': posts.order_by('date')[:3]
    }
    return render(request, 'blog/post.html', context)


def podcastView(request, name):
    posts = models.Post.objects.all()
    post = models.Post.objects.get(post_url=name)
    categories = models.SubCategory.objects.all()

    context = {
        'post': post, 'category': 'case_studies',
        'related_posts': posts.order_by('date')[:3],
        'categories': categories,
    }
    return render(request, 'blog/podcast.html', context)


# for specific category
def categoryView(request, name):
    if '/' in name:
        name = name.rpartition('/')[0]

    if name == 'blogs':
        posts = models.Post.objects.filter(category=name)
        template_name = 'blog/blogs.html'
    elif name == 'podcast':
        posts = models.Post.objects.filter(category=name)
        template_name = 'blog/podcast.html'
    elif name == 'case_studies':
        posts = models.Post.objects.filter(category=name)
        template_name = 'blog/case_studies.html'
    else:
        name = (str(name)).replace('_', ' ')
        print(name)
        posts = models.Post.objects.filter(sub_categories__sub_category__iexact=name)
        template_name = 'blog/index.html'

    case_studies = models.Post.objects.filter(sub_categories__sub_category=name, category='Case Studies')
    categories = models.SubCategory.objects.all()

    context = {
        'blogs': posts.order_by('-date'),
        'important_posts': posts.order_by('-date'),
        'recent_posts': posts,
        'case_studies': case_studies,
        'categories': categories,
    }

    return render(request, template_name, context)


def category_detailView(request, name1, name2):
    if '/' in name1:
        name1 = name1.rpartition('/')[0]
    if name1 == 'blogs':
        template_name = 'blog/blogs.html'
    else:
        template_name = 'blog/case_studies.html'

    posts = models.Post.objects.filter(category=name1, sub_category=name2)

    context = {
        'important_posts': posts.order_by('date'),
        'recent_posts': posts
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
