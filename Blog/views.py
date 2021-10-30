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


# Admin Section Start Here
@user_passes_test(permission_check, login_url='/accounts/login/')
def adminDashboardView(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts,

    }
    return render(request, 'admin_panel/blog/dashboard.html', context)


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminBlogFormView(request):
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

        for t in tags:
            if not models.Tags.objects.filter(tag=t).exists():
                new_tag = models.Tags.objects.create(tag=t)

        for i in inputItems:
            if i == "subCategory":
                subCategory = request.POST.get('subCategory')
            if i == "filterOption":
                filterOption = request.POST.get('filterOption')

        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Get Form Data
            # New System
            # Get Form Data
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

            post.save()
            add_tags = models.Tags.objects.filter(tag__in=tags)

            post.tag.add(*add_tags)

            # Old System
            # post_url = form.cleaned_data['post_url']
            # feature_image = form.cleaned_data['feature_image']
            # title = form.cleaned_data['title']
            # short_description = form.cleaned_data['short_description']
            # content = form.cleaned_data['content']
            # comment_option = form.cleaned_data['comment_option']
            #
            # cat = models.BlogCategory.objects.get(pk=category)
            #
            # add_tags = models.Tags.objects.filter(tag__in=tags)
            # instance = models.Post.objects.create(author=request.user, category=cat, feature_image=feature_image,
            #                                       post_url=post_url, title=title, short_description=short_description,
            #                                       content=content, comment_option=comment_option)
            # instance.tag.set(add_tags)
            # if subCategory:
            #     subcat = models.BlogSubCategory.objects.get(pk=subCategory)
            #     instance.sub_categories = subcat
            #     instance.save()
            # if filterOption:
            #     subfil = models.FilterOption.objects.get(pk=filterOption)
            #     instance.filter_option = subfil
            #     instance.save()

            return HttpResponseRedirect(reverse('admin_dashboard'))

    context = {
        'form': form,
        'tag_list': tag_list,
    }
    return render(request, 'admin_panel/blog/blogForm.html', context)


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminBlogEditFormView(request, id):
    current_post = models.Post.objects.get(id=id)
    form = forms.PostForm(instance=current_post)
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

        for t in tags:
            if not models.Tags.objects.filter(tag=t).exists():
                new_tag = models.Tags.objects.create(tag=t)

        for i in inputItems:
            if i == "subCategory":
                subCategory = request.POST.get('subCategory')
            if i == "filterOption":
                filterOption = request.POST.get('filterOption')

        form = forms.PostForm(request.POST, request.FILES, instance=current_post)
        if form.is_valid():
            # Get Form Data
            # New System
            # Get Form Data
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

            post.save()
            add_tags = models.Tags.objects.filter(tag__in=tags)

            post.tag.add(*add_tags)

            # Old System
            # post_url = form.cleaned_data['post_url']
            # feature_image = form.cleaned_data['feature_image']
            # title = form.cleaned_data['title']
            # short_description = form.cleaned_data['short_description']
            # content = form.cleaned_data['content']
            # comment_option = form.cleaned_data['comment_option']
            #
            # cat = models.BlogCategory.objects.get(pk=category)
            #
            # add_tags = models.Tags.objects.filter(tag__in=tags)
            # instance = models.Post.objects.create(author=request.user, category=cat, feature_image=feature_image,
            #                                       post_url=post_url, title=title, short_description=short_description,
            #                                       content=content, comment_option=comment_option)
            # instance.tag.set(add_tags)
            # if subCategory:
            #     subcat = models.BlogSubCategory.objects.get(pk=subCategory)
            #     instance.sub_categories = subcat
            #     instance.save()
            # if filterOption:
            #     subfil = models.FilterOption.objects.get(pk=filterOption)
            #     instance.filter_option = subfil
            #     instance.save()

            return HttpResponseRedirect(reverse('admin_dashboard'))

    context = {
        'form': form,
        'tag_list': tag_list,
    }
    return render(request, 'admin_panel/blog/blogForm.html', context)


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminBlogView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/blogView.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminCategoryListView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/categoryList.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminCategoryView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/categoryView.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminCommentListView(request):
    comments = models.Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'admin_panel/blog/commentList.html', context)


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminCommentView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/commentView.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminFilterOptionListView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/filterOptionList.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminFilterOptionView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/filterOptionView.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminSubCategoryListView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/subCategoryList.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminSubCategoryView(request):
    context = {

    }
    return render(request, 'admin_panel/blog/subCategoryView.html')


@user_passes_test(permission_check, login_url='/accounts/login/')
def adminNewPostView(request):
    form = forms.PostForm()
    tag_list = models.Tags.objects.all()
    subCategory = ''
    filterOption = ''
    subcat = ''
    subfil = ''
    print(request.POST)
    if request.method == 'POST':
        inputItems = request.POST
        category = request.POST.get('category')
        tags = request.POST.getlist('tagName')

        for t in tags:
            if not models.Tags.objects.filter(tag=t).exists():
                new_tag = models.Tags.objects.create(tag=t)

        for i in inputItems:
            if i == "subCategory":
                subCategory = request.POST.get('subCategory')
            if i == "filterOption":
                filterOption = request.POST.get('filterOption')

        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Get Form Data
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

            post.save()
            add_tags = models.Tags.objects.filter(tag__in=tags)

            for tl in add_tags:
                post.tag.add(tl)  # new

            return HttpResponseRedirect(reverse('index'))

    context = {
        'form': form,
        'tag_list': tag_list,
    }
    return render(request, 'blog/admin.html', context)


@user_passes_test(permission_check, login_url='accounts/login/')
def adminDeletePostView(request, id):
    post = models.Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(permission_check, login_url='accounts/login/')
def adminDeleteCommentView(request, id):
    comment = models.Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Admin Section End Here
def indexView(request):
    articles = models.Post.objects.filter(category__category__iexact='articles')
    case_studies = models.Post.objects.filter(category__category__iexact='case_studies')
    categories = models.BlogCategory.objects.all()
    subcategories = models.BlogSubCategory.objects.all()
    print(articles)
    print(case_studies)
    context = {
        'articles': articles.order_by('date')[:4],
        'case_studies': case_studies.order_by('date')[:4],
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'blog/index.html', context)


# these 3 functions for single post
def postView(request, name):
    posts = models.Post.objects.all()
    post = models.Post.objects.get(post_url=name)
    comments = models.Comment.objects.filter(post=post).order_by('-comment_date')
    reading_lists = models.ReadingList.objects.filter(user=request.user).values_list('post', flat=True)
    total = post.total_view
    category = str(request.path).split('/')[-3]
    post.total_view = total + 1
    post.save()

    context = {
        'post': post, 'category': category,
        'related_posts': posts.order_by('date')[:4],
        'comments': comments[:5],
        'comments_count': comments.count,
        'reading_lists': reading_lists,
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
    categories = models.BlogSubCategory.objects.all()

    context = {
        'post': post, 'category': 'case_studies',
        'related_posts': posts.order_by('date')[:3],
        'categories': categories,
    }
    return render(request, 'blog/post.html', context)


@login_required
def addToReadingListView(request, id):
    current_post = models.Post.objects.get(id=id)
    is_saved = models.ReadingList.objects.filter(user=request.user, post=current_post)
    if not is_saved:
        models.ReadingList.objects.get_or_create(user=request.user, post=current_post)
    else:
        is_saved.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# for specific category
def categoryView(request, name):

    posts = models.Post.objects.filter(Q(category__category__iexact=str(name).replace('_', ' ')) or Q(category__category__iexact=str(name)))
    cat_path = str(request.path).split('/')[-2]
    subcategories = models.BlogSubCategory.objects.filter(category__category__iexact=str(name).replace('_', ' ')).order_by('sub_category')
    reading_lists = models.ReadingList.objects.filter(user=request.user).values_list('post', flat=True)

    print(str(name).replace('_', ' ').title())
    context = {
        'posts': posts.order_by('-date'),
        'path': name,
        'cat_path': cat_path,
        'important_posts': posts.order_by('-total_view'),
        'subcategories': subcategories,
        'reading_lists': reading_lists,
    }

    return render(request, 'blog/category.html', context)


def category_detailView(request, name1, name2):
    posts = models.Post.objects.filter(category__category__iexact=str(name1).replace('_', ' '),
                                       sub_categories__sub_category__iexact=str(name2).replace('_', ' '))
    filter_options = models.FilterOption.objects.filter(
        sub_category__category__category__iexact=str(name1).replace('_', ' '),
        sub_category__sub_category__iexact=str(name2).replace('_', ' '))
    subcategories = models.BlogSubCategory.objects.filter(category__category__iexact=str(name1).replace('_', ' '))
    context = {
        'posts': posts.order_by('-date'),
        'cat_path': name1,
        'path2': name2,
        'important_posts': posts.order_by('-total_view')[:4],
        'subcategories': subcategories,
        'filter_options': filter_options,
    }
    return render(request, 'blog/category.html', context)


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
