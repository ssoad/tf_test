from django.urls import path
from PersonalSecurity import views

app_name = 'pcs_app'

urlpatterns = [
    path('', views.personalSecurityView, name='my_security_home'),

    path('concierge_cybersecurity/', views.conciergeCybersecurityView, name='concierge_cybersecurity'),
    path('cyber_investigation/', views.cyberInvestigationView, name='cyber_investigation'),
    path('osint_investigations/', views.OSIntInvestigationsView, name='osint_investigations'),

    path('cyber_crime_investigation/', views.cyberCrimeInvestigationView, name='cyber_crime_investigation'),
    path('incident_response_service/', views.incidentResponseServiceView, name='incident_response_service'),
    path('hack_recovery_service/', views.hackRecoveryServiceView, name='hack_recovery_service'),
    path('remove_malware_from_pc/', views.removeMalwareFromPCView, name='remove_malware_from_pc'),
    path('data_removal/', views.dataRemovalView, name='data_removal'),
    path('on_board/', views.onBoardView, name='on_board'),
    path('pricing/', views.pricingView, name='pricing'),
    path('faq/', views.faqView, name='faq'),
    path('vip_cyber_defense/', views.vipCyberDefenseView, name='vip_cyber_defense'),
    path('executive_protection/', views.executiveProtectionView, name='executive_protection'),
    path('cyber_security_for_government/', views.cyberSecurityForGovernmentView, name='cyber_security_for_government'),
    path('media_celebrities/', views.mediaCelebritiesView, name='media_celebrities'),
    path('site_map/', views.siteMapView, name='site_map'),

    # user panel
    path('pcs_user_dashboard/', views.userDashboardView, name='pcs_user_dashboard'),
    path('pcs_user_services/', views.userServicesView, name='pcs_user_services'),
    path('pcs_user_order_history/', views.userOrderHistoryView, name='pcs_user_order_history'),
    path('pcs_user_subscriptions/', views.userSubscriptionsView, name='pcs_user_subscriptions'),
    path('pcs_user_events/', views.userEventsView, name='pcs_user_events'),
    path('pcs_user_notifications/', views.userNotificationsView, name='pcs_user_notifications'),
    path('pcs_user_settings/', views.userSettingsView, name='pcs_user_settings'),
    path('pcs_appoinment/', views.pcsAppoinmentView, name='pcs_appoinment'),

# pcs admin panel
    path('pcs_admin_dashboard/',views.pcsAdminDashboard, name='pcs_admin_dashboard'),
    path('pcs_admin_services/',views.pcsAdminService, name='pcs_admin_services'),
    path('pcs_admin_revenue/',views.pcsAdminRevenue, name='pcs_admin_revenue'),
    path('pcs_admin_subscriptions/',views.pcsAdminSubscriptionList, name='pcs_admin_subscriptions'),
    path('pcs_admin_subscription_packages/',views.pcsAdminSubscriptionPack, name='pcs_admin_subscription_packages'),
    path('pcs_admin_reading_list/',views.pcsAdminReadingList, name='pcs_admin_reading_list'),
    path('pcs_admin_sub_services/',views.pcsAdminSubService, name='pcs_admin_sub_services'),
    path('pcs_admin_individual_users/',views.pcsAdminIndividualUser, name='pcs_admin_individual_users'),
    path('pcs_admin_individual_user_panel/',views.pcsAdminIndividualUserPanel, name='pcs_admin_individual_user_panel'),
    path('pcs_admin_list/',views.pcsAdminList, name='pcs_admin_list'),
    path('pcs_admin_profile/',views.pcsAdminProfile, name='pcs_admin_profile'),
    path('pcs_admin_user_interest/',views.pcsAdminUserInterest, name='pcs_admin_user_interest'),
    path('pcs_admin_training/',views.pcsAdminTraining, name='pcs_admin_training'),
    path('pcs_admin_course_detail/',views.pcsAdminCourseDetail, name='pcs_admin_course_detail'),
]
