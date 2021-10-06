from django.urls import path
from Blog import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('admin/', views.adminView, name='admin'),
    path('category/<name>/', views.categoryView, name='category'),
    path('category/<slug:name1>/<slug:name2>/', views.category_detailView, name='category_detail'),
    path('articles/<slug:name>/', views.blogsView, name='blogs'),
    path('case_studies/<slug:name>/', views.case_studiesView, name='case_studies'),
    path('podcast/<slug:name>/', views.podcastView, name='podcast'),
    path('filter_post_keyword/<str:type>/<str:keyword>/', views.filter_post_keywordView, name='filter_post_keyword'),
    path('filter_post_date/<str:type>/<str:range>/', views.filter_post_dateView, name='filter_post_date'),


]
