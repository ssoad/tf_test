import itertools

from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models
from BusinessSecurity import models as bcsmodels
from rest_framework import permissions, pagination, filters


# Create your views here.

class PostApi(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostSerializer


class CategoryApi(generics.ListAPIView):
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializer.CategorySerializer


class SubCategoryApi(generics.ListAPIView):
    # queryset = models.BlogSubCategory.objects.all()
    serializer_class = serializer.SubCategorySerializer

    def get_queryset(self):
        category = self.kwargs['id']
        return models.BlogSubCategory.objects.filter(category=category)


class FilterApi(generics.ListAPIView):
    # queryset = models.FilterOption.objects.all()
    serializer_class = serializer.FilterSerializer

    def get_queryset(self):
        category = self.kwargs['id']
        subcategory = self.kwargs['sub_id']
        return models.FilterOption.objects.filter(sub_category=subcategory, sub_category__category=category)


class Page(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5


class AllCommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['comment_date']


class CommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page

    def get_queryset(self):
        post = self.kwargs['post_id']
        return models.Comment.objects.filter(post=post)


class PackageListViewApi(generics.ListAPIView):
    serializer_class = serializer.PackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionBasedPackage.objects.filter(service_id=service_id)
