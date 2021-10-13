from django.urls import path
from Blog import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('category/<name>/', views.categoryView, name='category'),
    path('category/<str:name1>/<str:name2>/', views.category_detailView, name='category_detail'),
    path('post/<slug:name>/', views.postView, name='blogs'),
    path('case_studies/<slug:name>/', views.case_studiesView, name='case_studies'),
    path('podcast/<slug:name>/', views.podcastView, name='podcast'),
    path('filter_post_keyword/<str:type>/<str:keyword>/', views.filter_post_keywordView, name='filter_post_keyword'),
    path('filter_post_date/<str:type>/<str:range>/', views.filter_post_dateView, name='filter_post_date'),

    path('dashboard/', views.adminDashboardView, name='admin_dashboard'),
    path('new/', views.adminNewPostView, name='admin_new'),
    path('blogform/', views.adminBlogFormView, name='admin_blog_form'),
    path('blogformedit/<int:id>', views.adminBlogEditFormView, name='admin_blog_form_edit'),
    path('delete_post/<int:id>', views.adminDeletePostView, name='admin_blog_delete'),
    path('delete_comment/<int:id>', views.adminDeleteCommentView, name='admin_comment_delete'),
    path('blogview/', views.adminBlogView, name='admin_blog_view'),
    path('categorylist/', views.adminCategoryListView, name='admin_category_list'),
    path('categoryview/', views.adminCategoryView, name='admin_category_view'),
    path('commentlist/', views.adminCommentListView, name='admin_comment_list'),
    path('commentview/', views.adminCommentView, name='admin_comment_view'),
    path('filteroptionlist/', views.adminFilterOptionListView, name='admin_filter_option'),
    path('filteroptionview/', views.adminFilterOptionView, name='admin_filter_view'),
    path('subcategorylist/', views.adminSubCategoryListView, name='admin_subcategory_list'),
    path('subcategoryview/', views.adminSubCategoryView, name='admin_subcategory_view'),
]
