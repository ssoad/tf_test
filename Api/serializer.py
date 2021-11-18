from rest_framework import serializers
from Blog import models
from BusinessSecurity import models as bcsmodels


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name')
    category_name = serializers.CharField(source='category.category')

    class Meta:
        model = models.Post
        fields = ['id', 'post_url', 'title', 'feature_image', 'short_description', 'content', 'comment_option', 'date',
                  'updated_date', 'total_view', 'author', 'author_name', 'category', 'category_name', 'sub_categories',
                  'filter_option', 'tag']


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
    author = serializers.CharField(source='user.full_name', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id', 'comment', 'comment_date', 'user', 'post', 'author', 'post_title']


class BlogFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class PackageListSerializer(serializers.ModelSerializer):
    feature_subscription = serializers.StringRelatedField(many=True)
    service_name = serializers.CharField(source='service_id.service_title')

    class Meta:
        model = bcsmodels.SubscriptionBasedPackage
        fields = ['id', 'service_id', 'service_name', 'package_name', 'servers', 'websites', 'workstations', 'duration',
                  'duration_type', 'feature_subscription', 'price', ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.Service
        fields = ['service_title']


class SubServiceSerializer(serializers.ModelSerializer):
    # fields = serializers.StringRelatedField(many=True)
    # subservice_info = serializers.CharField(source='subservice.title')
    service_name = serializers.CharField(source='service.service_title')

    class Meta:
        model = bcsmodels.SubService
        fields = ['id', 'title', 'description', 'total_customer', 'service', 'service_name']
        # exclude = ['fields']
        # depth = 1


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SelectChoiceRelation
        # fields = '__all__'
        exclude = ['input_field']
        depth = 2


class SubServiceInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SubServiceInput
        # fields = ('id', 'inputfield', 'choices')
        exclude = ['subservice']
        depth = 1


class UserSubServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.Order
        fields = '__all__'
        # depth = 2
