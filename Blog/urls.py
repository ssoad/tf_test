from django.urls import path, include
from Blog import views


urlpatterns = [
    path('', views.indexView, name='index'),

    path('tinymce/', include('tinymce.urls')),
    path('category/', views.categoryView, name='category'),
    path('category/<name>/', views.categoryView, name='category'),
    path('category/<str:name1>/<str:name2>/', views.category_detailView, name='category_detail'),
    path('category/<str:name1>/<str:name2>/<str:name3>/', views.category_detailFilterView, name='category_detail_filter'),
    path('articles/', views.postView, name='articles'),
    path('articles/<slug:name>/', views.postView, name='articles'),
    path('case_studies/', views.postView, name='case_studies'),
    path('case_studies/<slug:name>/', views.postView, name='case_studies'),
    path('podcast/', views.postView, name='podcast'),
    path('podcast/<slug:name>/', views.postView, name='podcast'),
    path('add_to_reading_list/', views.addToReadingListView, name='add_to_reading_list'),
    path('add_to_reading_list/<id>/', views.addToReadingListView, name='add_to_reading_list'),
    path('filter_post_keyword/<str:type>/<str:keyword>/', views.filter_post_keywordView, name='filter_post_keyword'),
    path('filter_post_date/<str:type>/<str:range>/', views.filter_post_dateView, name='filter_post_date'),

    path('dashboard/', views.adminDashboardView, name='admin_dashboard'),
    path('new/', views.adminNewPostView, name='admin_new'),
    path('blogform/', views.adminBlogFormView, name='admin_blog_form'),
    path('blogformedit/', views.adminBlogEditFormView, name='admin_blog_form_edit'),
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

    path('category_delete/', views.categoryDeleteView, name='category_delete'),
    path('category_delete/<id>/', views.categoryDeleteView, name='category_delete'),
    path('subcategory_delete/', views.subCategoryDeleteView, name='subcategory_delete'),
    path('subcategory_delete/<id>/', views.subCategoryDeleteView, name='subcategory_delete'),
    path('filter_delete/', views.filterDeleteView, name='filter_delete'),
    path('filter_delete/<id>/', views.filterDeleteView, name='filter_delete'),
]
