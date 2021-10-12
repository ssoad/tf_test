from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from BusinessSecurity import forms, models
from Account.models import User, Permissions
from Account.forms import SelectPermissionForm, SelectBCSPermissionForm


# Create your views here.
def superuser_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


# def main_super_admin_permission_check(user):
#     return user.is_superuser or (
#                 user.permission_user.is_superadmin and user.permission_user.is_admin and user.permission_user.is_moderator and user.permission_user.is_editor)


def main_admin_permission_check(user):
    return user.is_superuser or ((
                                             user.permission_user.is_superadmin or user.permission_user.is_admin or user.permission_user.is_moderator or user.permission_user.is_editor) and user.permission_user.admin_type == 'main_admin')


def bcs_admin_permission_check(user):
    try:
        return user.is_superuser or ((user.permission_user.is_superadmin or user.permission_user.is_admin or user.permission_user.is_moderator or user.permission_user.is_editor) and (user.permission_user.admin_type == 'bcs_admin' or user.permission_user.admin_type == 'main_admin'))
    except:
        return user.is_superuser

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
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/dashboard.html', context)


@login_required
def userServicesView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/services.html', context)


@login_required
def userOrderHistoryView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/order_history.html', context)


@login_required
def bcsUserMyTeamView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/my_team.html', context)


@login_required
def userSubscriptionsView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/events.html', context)


@login_required
def userNotificationsView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/notifications.html', context)


@login_required
def userSettingsView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/settings.html', context)


@login_required
def employeeTrainingProgramView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/thanks.html', context)


@login_required
def bcsAppointmentView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_app:bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    elif request.user.is_bcs:
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
@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminDashboardView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/dashboard.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminProfileView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/myProfile.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminOrdersView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/orders.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminNotificationView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/notification.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminEventsView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/eventWebinar.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminEventDetailView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/eventDetail.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminSupportView(request):
    permission_form = SelectPermissionForm()
    admin_list = Permissions.objects.all()

    if request.method == 'POST':
        permission_form = SelectPermissionForm(request.POST)
        if permission_form.is_valid():
            permission_form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'permission_form': permission_form,
        'admin_list': admin_list,
    }
    return render(request, 'admin_panel/mainTF/support.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminSupportDeleteView(request, id):
    current_permission = Permissions.objects.get(id=id)
    current_permission.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminSupportStuffView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/supportStuffView.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminTicketsView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/allTickets.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminTicketsDetailView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/ticketView.html', context)


# BCS Admin Secction
@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminDashboardView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/dashboard.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceCategoryView(request):
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
    return render(request, 'admin_panel/bcsTF/serviceCategory.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceCategoryDeleteView(request, id):
    current_category = models.ServiceCategory.objects.get(id=id)
    current_category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceCategoryEditView(request, id):
    current_category = models.ServiceCategory.objects.get(id=id)
    form = forms.AddServiceCategoryForm(instance=current_category)

    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(request.POST, instance=current_category)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_app:bcs_admin_services_category'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceView(request):
    form = forms.AddServiceForm()
    services = models.Service.objects.all()
    if request.method == 'POST':
        form = forms.AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/service.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceDeleteView(request, id):
    current_service = models.Service.objects.get(id=id)
    current_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminServiceEditView(request, id):
    current_service = models.Service.objects.get(id=id)
    form = forms.AddServiceForm(instance=current_service)

    if request.method == 'POST':
        form = forms.AddServiceForm(request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_app:bcs_admin_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceView(request):
    form = forms.AddSubServiceForm()
    sub_services = models.SubService.objects.all()
    if request.method == 'POST':
        form = forms.AddSubServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'sub_services': sub_services,
    }
    return render(request, 'admin_panel/bcsTF/subService.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceDeleteView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    current_sub_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceEditView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    form = forms.AddSubServiceForm(instance=current_sub_service)

    if request.method == 'POST':
        form = forms.AddSubServiceForm(request.POST, instance=current_sub_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_app:bcs_admin_sub_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminReadingListView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/readingList.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminRevenueView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/revenue.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubscriptionListView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/subscriptionList.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubscriptionPack(request):
    form = forms.AddPackageForm()
    services = models.Service.objects.filter(is_subscription_based=True)
    if request.method == 'POST':
        form = forms.AddPackageForm(request.POST)
        form.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionPack.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminIndividualUser(request):
    users = models.User.objects.filter(is_bcs=True)
    context = {
        'users': users,
    }
    return render(request, 'admin_panel/bcsTF/users.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminIndividualUserPanel(request, id):
    current_user = models.User.objects.get(id=id)

    context = {
        'current_user': current_user,
    }
    return render(request, 'admin_panel/bcsTF/userPanel.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminList(request):
    permission_form = SelectBCSPermissionForm()
    admin_list = Permissions.objects.filter(admin_type='bcs_admin')
    super_admin_count = Permissions.objects.filter(admin_type='bcs_admin', is_superadmin=True).count()
    admin_count = Permissions.objects.filter(admin_type='bcs_admin', is_admin=True).count()
    moderator_count = Permissions.objects.filter(admin_type='bcs_admin', is_moderator=True).count()
    editor_count = Permissions.objects.filter(admin_type='bcs_admin', is_editor=True).count()
    if request.method == 'POST':
        try:
            permission_form = SelectBCSPermissionForm(request.POST)
            admin_type = 'bcs_admin'
            form = permission_form.save(commit=False)
            form.admin_type = admin_type
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        except:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'permission_form': permission_form,
        'admin_list': admin_list,
        'super_admin_count': super_admin_count,
        'admin_count': admin_count,
        'moderator_count': moderator_count,
        'editor_count': editor_count,
    }
    return render(request, 'admin_panel/bcsTF/adminUsers.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminProfile(request):
    return render(request, 'admin_panel/bcsTF/myProfile.html')


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminUserInterest(request):
    return render(request, 'admin_panel/bcsTF/userInterest.html')


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTraining(request):
    return render(request, 'admin_panel/bcsTF/training.html')


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminCourseDetail(request):
    return render(request, 'admin_panel/bcsTF/courseDetail.html')
