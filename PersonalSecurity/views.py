from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def personalSecurityView(request):
    context = {

    }
    return render(request, 'mspages/index.html', context)


def conciergeCybersecurityView(request):
    context = {

    }
    return render(request, 'mspages/pages/concierge_cybersecurity.html', context)


def cyberInvestigationView(request):
    context = {

    }
    return render(request, 'mspages/pages/cyber_investigation.html', context)


def OSIntInvestigationsView(request):
    context = {

    }
    return render(request, 'mspages/pages/osint_investigations.html', context)


def cyberCrimeInvestigationView(request):
    context = {

    }
    return render(request, 'mspages/pages/cyber_crime_investigation.html', context)


def incidentResponseServiceView(request):
    context = {

    }
    return render(request, 'mspages/pages/incident_response_service.html', context)


def hackRecoveryServiceView(request):
    context = {

    }
    return render(request, 'mspages/pages/hack_recovery_service.html', context)


def removeMalwareFromPCView(request):
    context = {

    }
    return render(request, 'mspages/pages/remove_malware_from_pc.html', context)


def dataRemovalView(request):
    context = {

    }
    return render(request, 'mspages/pages/data_removal.html', context)


def onBoardView(request):
    context = {

    }
    return render(request, 'mspages/pages/on_board.html', context)


def pricingView(request):
    context = {

    }
    return render(request, 'mspages/pages/pricing.html', context)


def faqView(request):
    context = {

    }
    return render(request, 'mspages/pages/faq.html', context)


def vipCyberDefenseView(request):
    context = {

    }
    return render(request, 'mspages/pages/vip_cyber_defense.html', context)


def executiveProtectionView(request):
    context = {

    }
    return render(request, 'mspages/pages/executive_protection.html', context)


def cyberSecurityForGovernmentView(request):
    context = {

    }
    return render(request, 'mspages/pages/cyber_security_for_government.html', context)


def mediaCelebritiesView(request):
    context = {

    }
    return render(request, 'mspages/pages/media_celebrities.html', context)


def siteMapView(request):
    context = {

    }
    return render(request, 'pages/sitemap.html', context)


@login_required
def userDashboardView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/dashboard.html', context)


@login_required
def userServicesView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/services.html', context)


@login_required
def userOrderHistoryView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/order_history.html', context)


@login_required
def userSubscriptionsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/events.html', context)


@login_required
def userNotificationsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/notifications.html', context)


@login_required
def userSettingsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/settings.html', context)


@login_required
def pcsAppoinmentView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/appoinment.html', context)

# New

#    pcs admin views

def pcsAdminDashboard(request):
    return render(request,'admin_panel/pcsTF/dashboard.html')

def pcsAdminService(request):
    return render(request,'admin_panel/pcsTF/service.html')

def pcsAdminSubService(request):
    return render(request,'admin_panel/pcsTF/subService.html')

def pcsAdminSubscriptionList(request):
    return render(request,'admin_panel/pcsTF/subscriptionList.html')

def pcsAdminSubscriptionPack(request):
    return render(request,'admin_panel/pcsTF/subscriptionPack.html')

def pcsAdminReadingList(request):
    return render(request,'admin_panel/pcsTF/readingList.html')

def pcsAdminRevenue(request):
    return render(request,'admin_panel/pcsTF/revenue.html')

def pcsAdminIndividualUser(request):
    return render(request,'admin_panel/pcsTF/users.html')

def pcsAdminIndividualUserPanel(request):
    return render(request,'admin_panel/pcsTF/userPanel.html')

def pcsAdminList(request):
    return render(request,'admin_panel/pcsTF/adminUsers.html')

def pcsAdminProfile(request):
    return render(request,'admin_panel/pcsTF/myProfile.html')

def pcsAdminUserInterest(request):
    return render(request,'admin_panel/pcsTF/userInterest.html')

def pcsAdminTraining(request):
    return render(request,'admin_panel/pcsTF/training.html')
def pcsAdminCourseDetail(request):
    return render(request,'admin_panel/pcsTF/courseDetail.html')