import itertools

from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models


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
