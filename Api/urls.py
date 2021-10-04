from django.urls import path
from Api import views

app_name = 'api_app'

urlpatterns = [
    path('posts/', views.PostApi.as_view(), name='post_api'),
    path('sub_category/', views.SubCategoryApi.as_view(), name='sub_category_api'),
]