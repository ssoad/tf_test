from rest_framework.serializers import ModelSerializer
from Blog import models


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = models.BlogSubCategory
        fields = '__all__'
