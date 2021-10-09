from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from BusinessSecurity import forms, models


# Create your views here.
def admin_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


def indexView(request):
    context = {

    }

    return render(request, 'index.html', context)


def getStartView(request):
    context = {

    }

    return render(request, 'pages/get_start.html', context)


def aboutUsView(request):
    context = {

    }

    return render(request, 'pages/aboutus.html', context)


def enterpriseCyberSecurityView(request):
    context = {

    }
    return render(request, 'pages/enterprise_cybersecurity.html', context)


# ---------------------------------------------

def enterpriseCyberSecurityView(request):
    context = {

    }
    return render(request, 'pages/enterprise_cybersecurity.html', context)


def vulnerabilityAssessmentView(request):
    context = {

    }
    return render(request, 'pages/vulnerability_assessment.html', context)


def redTeamPenetrationTestingView(request):
    context = {

    }
    return render(request, 'pages/red_team_penetration_testing.html', context)


def cybersecurityRiskAssessmentView(request):
    context = {

    }
    return render(request, 'pages/cybersecurity_risk_assessment.html', context)


def incidentResponseServiceView(request):
    context = {

    }
    return render(request, 'pages/incident_response_service.html', context)


def hackRecoveryServiceView(request):
    context = {

    }
    return render(request, 'pages/hack_recovery_service.html', context)


def bestMalwareRemovalView(request):
    context = {

    }
    return render(request, 'pages/best_malware_removal.html', context)


def digitalForensicInvestigationView(request):
    context = {

    }
    return render(request, 'pages/digital_forensic_investigation.html', context)


def complianceConsultingView(request):
    context = {

    }
    return render(request, 'pages/compliance_consulting.html', context)


def ISO27001View(request):
    context = {

    }
    return render(request, 'pages/iso27001.html', context)


def pciDssComplianceView(request):
    context = {

    }
    return render(request, 'pages/pci_dss_compliance.html', context)


def gdprComplianceView(request):
    context = {

    }
    return render(request, 'pages/gdpr_compliance.html', context)


def hippaComplianceConsultingView(request):
    context = {

    }
    return render(request, 'pages/hippa_compliance_consulting.html', context)


def smallBusinessCybersecurityView(request):
    context = {

    }
    return render(request, 'pages/small_business_cybersecurity.html', context)


def managedCybersecurityServiceView(request):
    context = {

    }
    return render(request, 'pages/managed_cybersecurity_service.html', context)


def plugAndPlayCyberCecurityView(request):
    context = {

    }
    return render(request, 'pages/plug_and_play_cyber_security.html', context)


def aboutUsView(request):
    context = {

    }
    return render(request, 'pages/aboutus.html', context)


def leaderView(request):
    context = {

    }
    return render(request, 'pages/leader.html', context)


def testimonialView(request):
    context = {

    }
    return render(request, 'pages/testimonial.html', context)


def partnerView(request):
    context = {

    }
    return render(request, 'pages/partner.html', context)


def partnerFaqView(request):
    context = {

    }
    return render(request, 'pages/partner_faq.html', context)


def franchiseView(request):
    context = {

    }
    return render(request, 'pages/franchise.html', context)


def franchiseFaqView(request):
    context = {

    }
    return render(request, 'pages/franchise_faq.html', context)


def investorView(request):
    context = {

    }
    return render(request, 'pages/investor.html', context)


def careerView(request):
    context = {

    }
    return render(request, 'pages/career.html', context)


def eventsView(request):
    context = {

    }
    return render(request, 'pages/events.html', context)


def policyView(request):
    context = {

    }
    return render(request, 'pages/policy.html', context)


def termsView(request):
    context = {

    }
    return render(request, 'pages/terms.html', context)


def BCSFormView(request):
    context = {

    }
    return render(request, 'pages/bcs_form.html', context)


def bPartnerView(request):
    context = {

    }
    return render(request, 'pages/bpartner.html', context)


def trustView(request):
    context = {

    }
    return render(request, 'pages/trust.html', context)


def findUsView(request):
    context = {

    }
    return render(request, 'pages/findus.html', context)


def appoinmentView(request):
    context = {

    }
    return render(request, 'pages/appoinment.html', context)


# Business Section
@login_required
def userDashboardView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/dashboard.html', context)


@login_required
def userServicesView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/services.html', context)


@login_required
def userOrderHistoryView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/order_history.html', context)


@login_required
def bcsUserMyTeamView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/my_team.html', context)


@login_required
def userSubscriptionsView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/events.html', context)


@login_required
def userNotificationsView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/notifications.html', context)


@login_required
def userSettingsView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/settings.html', context)


@login_required
def employeeTrainigProgramView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/thanks.html', context)


@login_required
def bcsAppoinmentView(request):
    context = {

    }
    return render(request, 'user_panel/bcs/appoinment.html', context)


# Team Member Section
@login_required
def teamUserServicesView(request):
    context = {

    }
    return render(request, 'user_panel/team/services.html', context)


@login_required
def teamUserMyTeamView(request):
    context = {

    }
    return render(request, 'user_panel/team/my_team.html', context)


@login_required
def teamUserSubscriptionsView(request):
    context = {

    }
    return render(request, 'user_panel/team/subscribed.html', context)


@login_required
def teamUserEventsView(request):
    context = {

    }
    return render(request, 'user_panel/team/events.html', context)


@login_required
def teamUserNotificationsView(request):
    context = {

    }
    return render(request, 'user_panel/team/notifications.html', context)


@login_required
def teamUserSettingsView(request):
    context = {

    }
    return render(request, 'user_panel/team/settings.html', context)


@login_required
def emailInvitationView(request):
    context = {

    }
    return render(request, 'user_panel/team/thanks.html', context)


# Main Admin Sections
@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminDashboardView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/dashboard.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminProfileView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/myProfile.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminOrdersView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/orders.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminNotificationView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/notification.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminEventsView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/eventWebinar.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminEventDetailView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/eventDetail.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminSupportView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/support.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminSupportStuffView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/supportStuffView.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminTicketsView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/allTickets.html', context)


@user_passes_test(admin_permission_check, login_url='/accounts/login/')
def mainAdminTicketsDetailView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/ticketView.html', context)


# BCS Admin Secction

def bcsAdminDashboardView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/dashboard.html', context)


def bcsAdminServiceView(request):
    categories = models.ServiceCategory.objects.all()
    form = forms.AddServiceCategoryForm()

    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'admin_panel/bcsTF/service.html', context)


def bcsAdminSubServiceView(request):
    form = forms.AddServiceForm()
    if request.method == 'POST':
        print(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/subService.html', context)


def bcsAdminReadingListView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/readingList.html', context)


def bcsAdminRevenueView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/revenue.html', context)


def bcsAdminSubscriptionListView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/subscriptionList.html', context)


# New

#    main admin views

def mainAdminDashboard(request):
    return render(request,'admin_panel/mainTF/dashboard.html')

def mainAdminProfile(request):
    return render(request,'admin_panel/mainTF/myProfile.html')

def mainAdminOrders(request):
    return render(request,'admin_panel/mainTF/orders.html')

def mainAdminNotification(request):
    return render(request,'admin_panel/mainTF/notification.html')

def mainAdminEvents(request):
    return render(request,'admin_panel/mainTF/eventWebinar.html')

def mainAdminEventDetail(request):
    return render(request,'admin_panel/mainTF/eventDetail.html')

def mainAdminSupport(request):
    return render(request,'admin_panel/mainTF/support.html')

def mainAdminSupportStuff(request):
    return render(request,'admin_panel/mainTF/supportStuffView.html')

def mainAdminTickets(request):
    return render(request,'admin_panel/mainTF/allTickets.html')

def mainAdminTicketsdetail(request):
    return render(request,'admin_panel/mainTF/ticketView.html')


#    bcs admin views

def bcsAdminDashboard(request):
    return render(request,'admin_panel/bcsTF/dashboard.html')

def bcsAdminService(request):
    return render(request,'admin_panel/bcsTF/service.html')

def bcsAdminSubService(request):
    return render(request,'admin_panel/bcsTF/subService.html')

def bcsAdminSubscriptionList(request):
    return render(request,'admin_panel/bcsTF/subscriptionList.html')

def bcsAdminSubscriptionPack(request):
    return render(request,'admin_panel/bcsTF/subscriptionPack.html')

def bcsAdminReadingList(request):
    return render(request,'admin_panel/bcsTF/readingList.html')

def bcsAdminRevenue(request):
    return render(request,'admin_panel/bcsTF/revenue.html')

def bcsAdminIndividualUser(request):
    return render(request,'admin_panel/bcsTF/users.html')

def bcsAdminIndividualUserPanel(request):
    return render(request,'admin_panel/bcsTF/userPanel.html')

def bcsAdminList(request):
    return render(request,'admin_panel/bcsTF/adminUsers.html')

def bcsAdminProfile(request):
    return render(request,'admin_panel/bcsTF/myProfile.html')

def bcsAdminUserInterest(request):
    return render(request,'admin_panel/bcsTF/userInterest.html')

def bcsAdminTraining(request):
    return render(request,'admin_panel/bcsTF/training.html')
def bcsAdminCourseDetail(request):
    return render(request,'admin_panel/bcsTF/courseDetail.html')
