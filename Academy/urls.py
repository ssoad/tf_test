from django.urls import path
from Academy import views



urlpatterns = [
    path('', views.academyHomeView, name='academy_home'),

    path('ccsp/', views.ccspView, name='ccsp'),

    path('academy_faq/', views.academyFAQView, name='academy_faq'),
    path('corporate_training/', views.corporateTrainingView, name='corporate_training'),
    path('law_enforcement/', views.corporateTrainingView, name='law_enforcement'),
    path('educational_institute/', views.educationalInstituteView, name='educational_institute'),

    path('download/', views.download_file, name='demo_download'),
    path('download/<str:path>', views.download_file, name='download'),
]
