from django.urls import path
from PersonalSecurity import views

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
    path('open_ticket/', views.openTicketView, name='open_ticket'),
    path('ticket_detail/', views.ticketDetailView, name='ticket_detail'),

    # user panel
    path('pcs_user_dashboard/', views.userDashboardView, name='pcs_user_dashboard'),
    path('pcs_user_services/', views.userServicesView, name='pcs_user_services'),
    path('pcs_user_reading_list/', views.userReadingListView, name='pcs_user_reading_list'),
    path('pcs_user_quotations_history/', views.userQuotationsHistoryView, name='pcs_user_quotations_history'),
    path('pcs_user_order_history/', views.userOrderHistoryView, name='pcs_user_order_history'),
    path('pcs_user_order_details/', views.userOrderDetailsView, name='pcs_user_order_details'),
    path('pcs_user_order_details/<id>/', views.userOrderDetailsView, name='pcs_user_order_details'),
    path('pcs_user_subscriptions/', views.userSubscriptionsView, name='pcs_user_subscriptions'),
    path('pcs_user_events/', views.userEventsView, name='pcs_user_events'),
    path('pcs_user_notifications/', views.userNotificationsView, name='pcs_user_notifications'),
    path('pcs_user_settings/', views.userSettingsView, name='pcs_user_settings'),
    path('pcs_appointment/', views.pcsAppointmentView, name='pcs_appointment'),

    # pcs academy user panel
    path('academy_user_courses/', views.UserCourses, name='academy_user_courses'),
    path('academy_user_courses/<id>/', views.UserCoursesDetails, name='academy_user_courses_details'),
    path('academy_my_courses/', views.myCourses, name='academy_my_courses'),
    path('academy_user_files/', views.UserFiles, name='academy_user_files'),
    path('academy_user_files/<id>/', views.UserFiles, name='academy_user_files'),

    # pcs admin panel
    path('pcs_admin_dashboard/', views.pcsAdminDashboard, name='pcs_admin_dashboard'),
    path('pcs_admin_services_category/', views.pcsAdminServiceCategoryView, name='pcs_admin_services_category'),
    path('pcs_admin_services_category_delete/<id>/', views.pcsAdminServiceCategoryDeleteView,
         name='pcs_admin_services_category_delete'),
    path('pcs_admin_services_category_edit/<id>/', views.pcsAdminServiceCategoryEditView,
         name='pcs_admin_services_category_edit'),
    path('pcs_admin_services/', views.pcsAdminServiceView, name='pcs_admin_services'),
    path('pcs_admin_services_delete/<id>/', views.pcsAdminServiceDeleteView, name='pcs_admin_services_delete'),
    path('pcs_admin_services_edit/<id>/', views.pcsAdminServiceEditView, name='pcs_admin_services_edit'),
    path('pcs_admin_sub_services/', views.pcsAdminSubServiceView, name='pcs_admin_sub_services'),
    path('pcs_admin_sub_services_delete/<id>/', views.pcsAdminSubServiceDeleteView,
         name='pcs_admin_sub_services_delete'),
    path('pcs_admin_sub_services_edit/<id>/', views.pcsAdminSubServiceEditView, name='pcs_admin_sub_services_edit'),
    path('pcs_admin_sub_services_form/', views.pcsSubServiceFormView, name='pcs_admin_sub_services_form'),
    path('pcs_admin_sub_services_form_delete/<id>/', views.pcsAdminSubServiceFormDeleteView,
         name='pcs_admin_sub_services_form_delete'),
    path('pcs_admin_sub_services_form_edit/<id>/', views.pcsAdminSubServiceFormEditView,
         name='pcs_admin_sub_services_form_edit'),

    path('pcs_admin_quotations/', views.pcsAdminQuotationsView, name='pcs_admin_quotations'),
    path('pcs_admin_orders/', views.pcsAdminOrdersView, name='pcs_admin_orders'),
    path('pcs_admin_new_order/', views.pcsAdminNewOrdersView, name='pcs_admin_new_order'),
    path('pcs_admin_order_detail/', views.pcsAdminOrdersDetailView, name='pcs_admin_order_detail'),
    path('pcs_admin_order_detail/<id>/', views.pcsAdminOrdersDetailView, name='pcs_admin_order_detail'),
    path('pcs_admin_order_new/', views.pcsAdminOrderNewView, name='pcs_admin_order_new'),
    path('pcs_admin_order_new/<id>/', views.pcsAdminOrderNewView, name='pcs_admin_order_new'),
    path('pcs_admin_order_attending/', views.pcsAdminOrderAttendingView, name='pcs_admin_order_attending'),
    path('pcs_admin_order_attending/<id>/', views.pcsAdminOrderAttendingView, name='pcs_admin_order_attending'),
    path('pcs_admin_order_completed/', views.pcsAdminOrderCompletedView, name='pcs_admin_order_completed'),
    path('pcs_admin_order_completed/<id>/', views.pcsAdminOrderCompletedView, name='pcs_admin_order_completed'),
    path('pcs_admin_order_canceled/', views.pcsAdminOrderCanceledView, name='pcs_admin_order_canceled'),
    path('pcs_admin_order_canceled/<id>/', views.pcsAdminOrderCanceledView, name='pcs_admin_order_canceled'),


    path('pcs_admin_all_tickets/', views.pcsAdminTicketsView, name='pcs_admin_all_tickets'),
    path('pcs_admin_tickets_detail/', views.pcsAdminTicketsDetailView, name='pcs_admin_tickets_detail'),
    path('pcs_admin_tickets_detail/<id>', views.pcsAdminTicketsDetailView, name='pcs_admin_tickets_detail'),

    path('pcs_admin_revenue/', views.pcsAdminRevenue, name='pcs_admin_revenue'),
    path('pcs_admin_subscriptions/', views.pcsAdminSubscriptionList, name='pcs_admin_subscriptions'),
    path('pcs_admin_subscription_packages/', views.pcsAdminSubscriptionPack, name='pcs_admin_subscription_packages'),
    path('pcs_admin_reading_list/', views.pcsAdminReadingList, name='pcs_admin_reading_list'),
    path('pcs_admin_sub_services/', views.pcsAdminSubService, name='pcs_admin_sub_services'),
    path('pcs_admin_individual_users/', views.pcsAdminIndividualUser, name='pcs_admin_individual_users'),
    path('pcs_admin_individual_user_panel/<id>/', views.pcsAdminIndividualUserPanel, name='pcs_admin_individual_user_panel'),
    path('pcs_admin_list/', views.pcsAdminList, name='pcs_admin_list'),
    path('pcs_admin_profile/', views.pcsAdminProfile, name='pcs_admin_profile'),
    path('pcs_admin_user_interest/', views.pcsAdminUserInterest, name='pcs_admin_user_interest'),
    path('pcs_admin_training/', views.pcsAdminTraining, name='pcs_admin_training'),
    path('pcs_admin_course_detail/', views.pcsAdminCourseDetail, name='pcs_admin_course_detail'),

    path('pcs_admin_training/', views.pcsAdminTraining, name='pcs_admin_training'),
    path('pcs_admin_training_delete/<id>/', views.pcsAdminTrainingDelete, name='pcs_admin_training_delete'),
    path('pcs_admin_training_edit/<id>/', views.pcsAdminTrainingEdit, name='pcs_admin_training_edit'),
    path('pcs_admin_course_detail/<id>/', views.pcsAdminCourseDetail, name='pcs_admin_course_detail'),
    path('pcs_admin_course_section_edit/<id>/', views.pcsAdminCourseSectionEdit, name='pcs_admin_course_section_edit'),
    path('pcs_admin_course_content_delete/<id>/', views.pcsAdminCourseContentDelete,
         name='pcs_admin_course_content_delete'),
    path('pcs_admin_course_content_edit/<id>/', views.pcsAdminCourseContentEdit,
         name='pcs_admin_course_content_edit'),
]
