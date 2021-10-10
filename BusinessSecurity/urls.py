from django.urls import path
from BusinessSecurity import views

app_name = 'bcs_app'

urlpatterns = [
    path('', views.indexView, name='index'),

    path('about_us', views.aboutUsView, name='about_us'),
    path('enterprise_cybersecurity', views.enterpriseCyberSecurityView, name='enterprise_cybersecurity'),
    path('vulnerability_assessment/', views.vulnerabilityAssessmentView, name='vulnerability_assessment'),
    path('red_team_penetration_testing/', views.redTeamPenetrationTestingView, name='red_team_penetration_testing'),
    path('cybersecurity_risk_assessment/', views.cybersecurityRiskAssessmentView, name='cybersecurity_risk_assessment'),
    path('incident_response_service/', views.incidentResponseServiceView, name='incident_response_services'),
    path('hack_recovery_service/', views.hackRecoveryServiceView, name='hack_recovery_services'),
    path('best_malware_removal/', views.bestMalwareRemovalView, name='best_malware_removal'),
    path('digital_forensic_investigation/', views.digitalForensicInvestigationView,
         name='digital_forensic_investigation'),
    path('compliance_consulting/', views.complianceConsultingView, name='compliance_consulting'),
    path('iso27001/', views.ISO27001View, name='iso27001'),
    path('pci_dss_compliance/', views.pciDssComplianceView, name='pci_dss_compliance'),
    path('gdpr_compliance/', views.gdprComplianceView, name='gdpr_compliance'),
    path('hippa_compliance_consulting/', views.hippaComplianceConsultingView, name='hippa_compliance_consulting'),
    path('small_business_cybersecurity/', views.smallBusinessCybersecurityView, name='small_business_cybersecurity'),
    path('managed_cybersecurity_service/', views.managedCybersecurityServiceView, name='managed_cybersecurity_service'),
    path('plug_and_play_cyber_security/', views.plugAndPlayCyberCecurityView, name='plug_and_play_cyber_security'),

    path('leader/', views.leaderView, name='leader'),
    path('testimonial/', views.testimonialView, name='testimonial'),
    path('partner/', views.partnerView, name='partner'),
    path('partner_faq/', views.partnerFaqView, name='partner_faq'),
    path('franchise/', views.franchiseView, name='franchise'),
    path('franchise_faq/', views.franchiseFaqView, name='franchise_faq'),
    path('investor/', views.investorView, name='investor'),
    path('career/', views.careerView, name='career'),
    path('events/', views.eventsView, name='events'),
    path('policy/', views.policyView, name='policy'),
    path('terms/', views.termsView, name='terms'),

    path('bcs_form/', views.BCSFormView, name='bcs_form'),
    path('bpartner/', views.bPartnerView, name='bpartner'),

    path('trust/', views.trustView, name='trust'),
    path('findus/', views.findUsView, name='findus'),

    path('get_start/', views.getStartView, name='get_start'),

    path('appoinment/', views.appoinmentView, name='appoinment'),
    # main admin panel

    path('main_admin_dashboard/', views.mainAdminDashboardView, name='main_admin_dashboard'),
    path('main_admin_profile/', views.mainAdminProfileView, name='main_admin_profile'),
    path('main_admin_orders/', views.mainAdminOrdersView, name='main_admin_orders'),
    path('main_admin_notification/', views.mainAdminNotificationView, name='main_admin_notification'),
    path('main_admin_events/', views.mainAdminEventsView, name='main_admin_events'),
    path('main_admin_event_detail/', views.mainAdminEventDetailView, name='main_admin_event_detail'),
    path('main_admin_support_view/', views.mainAdminSupportView, name='main_admin_support_view'),
    path('main_admin_stuff_view/', views.mainAdminSupportStuffView, name='main_admin_stuff_view'),
    path('main_admin_all_tickets/', views.mainAdminTicketsView, name='main_admin_all_tickets'),
    path('main_admin_tickets_detail/', views.mainAdminTicketsDetailView, name='main_admin_tickets_detail'),

    # bcs user panel
    path('bcs_user_dashboard/', views.userDashboardView, name='bcs_user_dashboard'),
    path('bcs_user_services/', views.userServicesView, name='bcs_user_services'),
    path('bcs_user_order_history/', views.userOrderHistoryView, name='bcs_user_order_history'),
    path('bcs_user_subscriptions/', views.userSubscriptionsView, name='bcs_user_subscriptions'),
    path('bcs_user_events/', views.userEventsView, name='bcs_user_events'),
    path('bcs_user_notifications/', views.userNotificationsView, name='bcs_user_notifications'),
    path('bcs_user_settings/', views.userSettingsView, name='bcs_user_settings'),
    path('bcs_user_my_team/', views.bcsUserMyTeamView, name='bcs_user_my_team'),
    path('employee_training_program/', views.employeeTrainigProgramView, name='employee_training_program'),


    path('bcs_appoinment/', views.bcsAppoinmentView, name='bcs_appoinment'),


    # bcs admin panel
    path('bcs_admin_dashboard/', views.bcsAdminDashboardView, name='bcs_admin_dashboard'),
    path('bcs_admin_revenue/', views.bcsAdminRevenueView, name='bcs_admin_revenue'),
    path('bcs_admin_subscriptions/', views.bcsAdminSubscriptionListView, name='bcs_admin_subscriptions'),
    path('bcs_admin_reading_list/', views.bcsAdminReadingListView, name='bcs_admin_reading_list'),
    path('bcs_admin_services_category/', views.bcsAdminServiceCategoryView, name='bcs_admin_services_category'),
    path('bcs_admin_services_category_delete/<id>', views.bcsAdminServiceCategoryDeleteView, name='bcs_admin_services_category_delete'),
    path('bcs_admin_services_category_edit/<id>', views.bcsAdminServiceCategoryEditView, name='bcs_admin_services_category_edit'),
    path('bcs_admin_services/', views.bcsAdminServiceView, name='bcs_admin_services'),
    path('bcs_admin_services_delete/<id>', views.bcsAdminServiceDeleteView, name='bcs_admin_services_delete'),
    path('bcs_admin_services_edit/<id>', views.bcsAdminServiceEditView, name='bcs_admin_services_edit'),
    path('bcs_admin_sub_services/', views.bcsAdminSubServiceView, name='bcs_admin_sub_services'),
    path('bcs_admin_sub_services_delete/<id>', views.bcsAdminSubServiceDeleteView, name='bcs_admin_sub_services_delete'),
    path('bcs_admin_sub_services_edit/<id>', views.bcsAdminSubServiceEditView, name='bcs_admin_sub_services_edit'),

# bcs admin panel
    path('bcs_admin_subscription_packages/',views.bcsAdminSubscriptionPack, name='bcs_admin_subscription_packages'),
    path('bcs_admin_individual_users/',views.bcsAdminIndividualUser, name='bcs_admin_individual_users'),
    path('bcs_admin_individual_user_panel/',views.bcsAdminIndividualUserPanel, name='bcs_admin_individual_user_panel'),
    path('bcs_admin_list/',views.bcsAdminList, name='bcs_admin_list'),
    path('bcs_admin_profile/',views.bcsAdminProfile, name='bcs_admin_profile'),
    path('bcs_admin_user_interest/',views.bcsAdminUserInterest, name='bcs_admin_user_interest'),
    path('bcs_admin_training/',views.bcsAdminTraining, name='bcs_admin_training'),
    path('bcs_admin_course_detail/',views.bcsAdminCourseDetail, name='bcs_admin_course_detail'),


    # team invidual user panel
    path('team_user_services/', views.teamUserServicesView, name='team_user_services'),
    path('team_user_my_team/', views.teamUserMyTeamView, name='team_user_my_team'),
    path('team_user_subscriptions/', views.teamUserSubscriptionsView, name='team_user_subscriptions'),
    path('team_user_events/', views.teamUserEventsView, name='team_user_events'),
    path('team_user_notifications/', views.teamUserNotificationsView, name='team_user_notifications'),
    path('team_user_settings/', views.teamUserSettingsView, name='team_user_settings'),
    path('email_invitation/', views.emailInvitationView, name='email_invitation'),
]
