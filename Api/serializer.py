from rest_framework import serializers
from Blog import models
from BusinessSecurity import models as bcsmodels
from Academy import models as coursemodels


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


class FeatureSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SubscriptionFeatures
        fields = '__all__'


class PackageListSerializer(serializers.ModelSerializer):
    # feature_subscription = serializers.StringRelatedField(many=True)
    feature_subscription = FeatureSubscriptionsSerializer(many=True)
    service_name = serializers.CharField(source='service_id.service_title')
    product_id = serializers.CharField(source='service_id.product_id')

    class Meta:
        model = bcsmodels.SubscriptionBasedPackage
        fields = '__all__'


class SubscriptionServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SubscriptionServices
        fields = '__all__'


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
        fields = ['id', 'title', 'total_customer', 'service', 'service_name']
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


class TeamPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.UsersBusiness
        fields = ['position', 'privilege']


class ServiceTFSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.Service
        fields = ['is_subscription_based']


class BCSAdminDashboardChartSerializer(serializers.ModelSerializer):
    service = ServiceTFSerializer(many=False, read_only=True)

    class Meta:
        model = bcsmodels.Order
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        data = super(BCSAdminDashboardChartSerializer, self).to_representation(instance)
        user = data.get('user')
        user.pop('password')
        return data


class SubServiceInputFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SubServiceInput
        fields = ['inputfield']
        depth = 1


class UserSubserviceInputSerializer(serializers.ModelSerializer):
    question = SubServiceInputFieldSerializer(source='inputfield')

    class Meta:
        model = bcsmodels.UserSubserviceInput
        fields = ['id', 'question', 'inputinfo']
        depth = 2


class SubscriptionSerializer(serializers.ModelSerializer):
    order_details = UserSubserviceInputSerializer(source='subserviceinput', many=True)
    order_price = serializers.CharField(source='orderprice_order.price')

    class Meta:
        model = bcsmodels.Order
        fields = ['id', 'service', 'order_details', 'order_price', 'order_status']
        depth = 2

    def to_representation(self, instance):
        data = super(SubscriptionSerializer, self).to_representation(instance)
        service = data.get('service')
        service.pop('category_choice')
        service.pop('service_icon')
        service.pop('short_description')
        service.pop('service_header')
        service.pop('service_body')
        service.pop('service_footer')
        service.pop('has_sub_service')
        service.pop('is_subscription_based')
        service.pop('total_customer')
        return data


class SubscriptionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = bcsmodels.SubscriptionOrder
        fields = '__all__'


class PCSCoursePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = coursemodels.CoursePurchase
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }


class BCSCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = coursemodels.BCSCourse
        fields = '__all__'


class BCSCourseFeatureSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = coursemodels.PackageFeatures
        fields = '__all__'


class BCSCoursePackageListSerializer(serializers.ModelSerializer):
    # feature_subscription = serializers.StringRelatedField(many=True)
    # feature_subscription = BCSCourseFeatureSubscriptionsSerializer(many=True)
    service_name = serializers.CharField(source='service_id.service_title')
    product_id = serializers.CharField(source='service_id.product_id')

    class Meta:
        model = coursemodels.CoursePackage
        fields = '__all__'
