from django.urls import path
from Account import views

app_name = 'account_app'

urlpatterns = [
    # path('login/', views.loginView, name='login'),
    # path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.profileView, name='profile'),
]
