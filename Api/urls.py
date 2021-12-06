from django.urls import path
from Api import views

app_name = 'api_app'

urlpatterns = [
    path('blogs/posts/', views.PostApi.as_view(), name='post_api'),
    path('blogs/category/', views.CategoryApi.as_view(), name='category_api'),
    path('blogs/category/<id>/', views.SubCategoryApi.as_view(), name='sub_category_api'),
    path('blogs/category/<id>/<sub_id>/', views.FilterApi.as_view(), name='sub_filter_api'),
    path('blogs/comment/', views.AllCommentCreateViewApi.as_view(), name='all_comment_create_view_api'),
    path('blogs/comment/<post_id>/', views.CommentCreateViewApi.as_view(), name='comment_create_view_api'),
    path('blogs/filter/<category>/<text>/', views.BlogFilterApiView.as_view(), name='blog_filter_view_api'),
    path('blogs/filter/date/<category>/<text>/', views.BlogFilterDateApiView.as_view(), name='blog_filter_date_view_api'),

    path('bcs/package/<id>/', views.PackageListViewApi.as_view(), name='package_list_api'),
    path('bcs/services/<cat>/', views.ServiceListApiView.as_view(), name='service_list_api'),
    path('bcs/sub_service/<id>/', views.SubServiceApiView.as_view(), name='subservice_list_api'),
    path('bcs/sub_service_input/<id>/', views.SubServiceInputApiView.as_view(), name='subservice_input_list_api'),
    path('bcs/choice_field/<id>/', views.ChoiceApiView.as_view(), name='choice_field'),
    path('bcs/user_order/<id>/', views.UserSubServiceOrderApiView.as_view(), name='user_order'),
]