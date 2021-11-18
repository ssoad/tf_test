import itertools

from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models
from BusinessSecurity import models as bcsmodels
from rest_framework import permissions, pagination, filters
from datetime import date
from django.db.models import Q


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


class BlogFilterApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        return models.Post.objects.filter(
            Q(category__category__iexact=category, title__icontains=text) | Q(category__category__iexact=category,
                                                                              short_description__icontains=text))


class BlogFilterDateApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer
    today = date.today()

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        if text == 'month':
            return models.Post.objects.filter(category__category__iexact=category, date__month=self.today.month)
        elif text == 'year':
            return models.Post.objects.filter(category__category__iexact=category, date__year=self.today.year)


class PackageListViewApi(generics.ListAPIView):
    serializer_class = serializer.PackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionBasedPackage.objects.filter(service_id=service_id)


class ServiceListApiView(generics.ListAPIView):
    serializer_class = serializer.ServiceSerializer
    queryset = bcsmodels.Service.objects.all()

    # def get_queryset(self):
    #     service_id = self.kwargs['id']
    #     return bcsmodels.Service.objects.all()


class SubServiceApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceSerializer

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubService.objects.filter(service_id=service_id)


class SubServiceInputApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceInputSerializer

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubServiceInput.objects.filter(subservice_id=service_id)


class ChoiceApiView(generics.ListAPIView):
    serializer_class = serializer.ChoiceSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return bcsmodels.SelectChoiceRelation.objects.filter(input_field_id=id)


class UserSubServiceOrderApiView(generics.ListAPIView):
    serializer_class = serializer.UserSubServiceOrderSerializer

    def get_queryset(self):
        subservice_id = self.kwargs['id']
        return bcsmodels.Order.objects.filter(id=subservice_id)
