from django.urls import path
from Api import views

app_name = 'api_app'

urlpatterns = [
    path('blogs/posts/', views.PostApi.as_view(), name='post_api'),
    path('blogs/category/', views.CategoryApi.as_view(), name='category_api'),
    path('blogs/category/<id>', views.SubCategoryApi.as_view(), name='sub_category_api'),
    path('blogs/category/<id>/<sub_id>', views.FilterApi.as_view(), name='sub_filter_api'),
]