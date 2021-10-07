from rest_framework import serializers
from Blog import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    has_subcategory = serializers.SerializerMethodField('_check_subcategories')

    def _check_subcategories(self, category):
        has_subcategories = getattr(category, 'has_subcategories')
        return has_subcategories

    class Meta:
        model = models.BlogCategory
        fields = ['id', 'category', 'has_subcategory']


class SubCategorySerializer(serializers.ModelSerializer):
    has_filter = serializers.SerializerMethodField('_check_filter')

    def _check_filter(self, filters):
        has_filters = getattr(filters, 'has_filter')
        return has_filters

    class Meta:
        model = models.BlogSubCategory
        fields = ['id', 'sub_category', 'has_filter']


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilterOption
        fields = ['id', 'filter_name']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.first_name', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id', 'comment', 'comment_date', 'user', 'post', 'author', 'post_title']
