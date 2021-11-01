from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from BusinessSecurity import forms, models
from Academy.forms import CourseCreateForm, SectionCreateForm, ContentCreateForm
from Account.models import User, Permissions, Interest
from Account.forms import SelectPermissionForm, SelectBCSPermissionForm, InterestForm
from Academy.models import Course, Section, Content
from django.core.paginator import Paginator


# Create your views here.
def superuser_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


# def main_super_admin_permission_check(user):
#     return user.is_superuser or (
#                 user.permission_user.is_superadmin and user.permission_user.is_admin and user.permission_user.is_moderator and user.permission_user.is_editor)


def main_admin_permission_check(user):
    try:
        return user.is_superuser or ((
                                             user.permission_user.is_superadmin or user.permission_user.is_admin or user.permission_user.is_moderator or user.permission_user.is_editor) and user.permission_user.admin_type == 'main_admin')
    except:
        return user.is_superuser


def bcs_admin_permission_check(user):
    try:
        return user.is_superuser or ((
                                             user.permission_user.is_superadmin or user.permission_user.is_admin or user.permission_user.is_moderator or user.permission_user.is_editor) and (
                                             user.permission_user.admin_type == 'bcs_admin' or user.permission_user.admin_type == 'main_admin'))
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
def createBusinessView(request):
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
                return HttpResponseRedirect(reverse('bcs_user_dashboard'))

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    else:
        return HttpResponseRedirect(reverse('bcs_user_dashboard'))


@login_required
def userDashboardView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        events = models.Events.objects.filter(status='active')
        registered_event = models.RegisteredEvents.objects.filter(user=request.user).values_list('event', flat=True)

        context = {
            'events': events,
            'registered_event': registered_event,
        }
        return render(request, 'user_panel/bcs/dashboard.html', context)


@login_required
def userServicesView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        service_category = models.ServiceCategory.objects.all()
        services = models.Service.objects.all()
        sub_services = models.SubService.objects.all()
        if request.method == 'POST':
            data_list = request.POST
            # print(request.POST)
            current_service = get_object_or_404(models.Service, service_title=data_list['service_name'])

            for data in data_list:
                if data != 'csrfmiddlewaretoken' and data != 'service_name':
                    current_input = models.SubServiceInput.objects.get(id=data)
                    input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                            inputinfo=data_list[data])
                    input_data.save()
                    order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                               service=current_service)
                    print(order)
                    order[0].subserviceinput.add(input_data)

                    # if order[0].service != input_data.inputfield.subservice.service:
                    #
                    # for order_service in order[0].subserviceinput.all():
                    #     if order_service.inputfield.subservice.service != input_data.inputfield.subservice.service:
                    #         new_order = models.Order.objects.create(user=request.user)
                    #         new_order.subserviceinput.add(input_data)
                    #         print('new')
                    #         break
                    #     else:
                    #         order[0].subserviceinput.add(input_data)
                    #         print('old')
        context = {
            'service_category': service_category,
            'services': services,
            'sub_services': sub_services,
            'services_headings': list(services.values_list('service_title', flat=True)),
        }
        return render(request, 'user_panel/bcs/services.html', context)


@login_required
def userOrderHistoryView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/order_history.html', context)


@login_required
def bcsUserMyTeamView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/my_team.html', context)


@login_required
def userSubscriptionsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        registered_event = models.RegisteredEvents.objects.filter(user=request.user).values_list('event', flat=True)
        events = models.Events.objects.filter(category='for_business_security',
                                              registered_event_event__user=request.user)
        context = {
            'events': events,
            'registered_event': registered_event,
        }
        return render(request, 'user_panel/bcs/events.html', context)


@login_required
def userEventRegisterView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        current_event = models.Events.objects.get(id=id)
        is_register = models.RegisteredEvents.objects.filter(user=request.user, event=current_event)
        if not is_register:
            models.RegisteredEvents.objects.get_or_create(user=request.user, event=current_event)
        else:
            is_register.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def userNotificationsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/notifications.html', context)


@login_required
def userSettingsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/settings.html', context)


@login_required
def employeeTrainingProgramView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/thanks.html', context)


@login_required
def bcsAppointmentView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

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
    form = forms.EventCreateForm()
    events = models.Events.objects.all()
    if request.method == 'POST':
        form = forms.EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'events': events,
    }
    return render(request, 'admin_panel/mainTF/eventWebinar.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminEventsDeleteView(request, id):
    current_event = models.Events.objects.get(id=id)
    current_event.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminEventsEditView(request, id):
    current_event = models.Events.objects.get(id=id)
    form = forms.EventCreateForm(instance=current_event)
    if request.method == 'POST':
        form = forms.EventCreateForm(request.POST, instance=current_event)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('main_admin_events'))
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/mainTF/editForm.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/')
def mainAdminEventDetailView(request, id):
    event = models.Events.objects.get(id=id)
    context = {
        'event': event,
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

            return HttpResponseRedirect(reverse('bcs_admin_services_category'))

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

            return HttpResponseRedirect(reverse('bcs_admin_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceView(request):
    form = forms.AddSubServiceForm()
    sub_services = models.SubService.objects.all()
    print(request.POST)
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

            return HttpResponseRedirect(reverse('bcs_admin_sub_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsSubServiceFormView(request):
    form = forms.AddForm()
    form_lists = models.InputFields.objects.all()
    print(request.POST)
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'form_lists': form_lists,
    }
    return render(request, 'admin_panel/bcsTF/subserviceForms.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceFormDeleteView(request, id):
    input_field = models.InputFields.objects.get(id=id)
    input_field.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubServiceFormEditView(request, id):
    current_input_field = models.InputFields.objects.get(id=id)
    form = forms.AddForm(instance=current_input_field)

    if request.method == 'POST':
        form = forms.AddForm(request.POST, instance=current_input_field)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_sub_services_form'))

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
    form2 = forms.AddPackageFeatureForm()
    services = models.Service.objects.filter(is_subscription_based=True)
    if request.method == 'POST':
        if 'package-btn' in request.POST:
            form = forms.AddPackageForm(request.POST)
            form.save()
        elif 'feature-btn' in request.POST:
            form2 = forms.AddPackageFeatureForm(request.POST)
            form2.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'form2': form2,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionPack.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubscriptionPackEdit(request, id):
    current_package = models.SubscriptionBasedPackage.objects.get(id=id)
    package_features = models.SubscriptionFeatures.objects.filter(package=current_package)
    form = forms.AddPackageForm(instance=current_package)
    form2 = forms.AddIndividualPackageFeatureForm()
    if request.method == 'POST':
        if 'package-btn' in request.POST:
            form = forms.AddPackageForm(request.POST, instance=current_package)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('bcs_admin_subscription_packages'))
        elif 'feature-btn' in request.POST:
            print(request.POST)
            current_feature = models.SubscriptionFeatures.objects.get(id=request.POST.get('feature_id'))
            current_feature.feature_name = request.POST.get('feature_name')
            current_feature.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'add-feature-btn' in request.POST:
            form2 = forms.AddIndividualPackageFeatureForm(request.POST)
            if form2.is_valid():
                feature = form2.save(commit=False)
                feature.package = current_package
                feature.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'form': form,
        'form2': form2,
        'package_features': package_features,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionPackEdit.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubscriptionPackDelete(request, id):
    current_package = models.SubscriptionBasedPackage.objects.get(id=id)
    current_package.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSubscriptionPackFeatureDelete(request, id):
    current_feature = models.SubscriptionFeatures.objects.get(id=id)
    current_feature.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


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
def bcsAdminEdit(request, id):
    current_admin = Permissions.objects.get(id=id)
    permission_form = SelectBCSPermissionForm(instance=current_admin)
    if request.method == 'POST':
        permission_form = SelectBCSPermissionForm(request.POST, instance=current_admin)
        if permission_form.is_valid():
            permission_form.save()
            return HttpResponseRedirect(reverse('bcs_admin_list'))
    context = {
        'form': permission_form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminProfile(request):
    return render(request, 'admin_panel/bcsTF/myProfile.html')


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminUserInterest(request):
    users_list = User.objects.all()
    interests = Interest.objects.filter(user__is_bcs=True)
    context = {
        'users_list': users_list,
        'interests': interests,
    }
    return render(request, 'admin_panel/bcsTF/userInterest.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminSingleUserInterest(request, id):
    selected_interest = Interest.objects.get(id=id)
    form = InterestForm(instance=selected_interest)
    if request.method == 'POST':
        form = InterestForm(request.POST, instance=selected_interest)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bcs_admin_user_interest'))

    context = {
        'selected_interest': selected_interest,
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTraining(request):
    form = CourseCreateForm()
    courses = Course.objects.filter(course_type='Business')
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_type = 'Business'
            course.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'courses': courses,
    }
    return render(request, 'admin_panel/bcsTF/training.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTrainingDelete(request, id):
    current_course = Course.objects.get(id=id)
    current_course.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTrainingEdit(request, id):
    current_course = Course.objects.get(id=id)
    form = CourseCreateForm(instance=current_course)

    if request.method == 'POST':
        form = CourseCreateForm(request.POST, instance=current_course)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('bcs_admin_training'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminCourseDetail(request, id):
    course = Course.objects.get(id=id)
    sections = Section.objects.filter(course=course)
    form = SectionCreateForm()
    form2 = ContentCreateForm()
    if request.method == 'POST':
        if 'add_section' in request.POST:
            form = SectionCreateForm(request.POST)
            if form.is_valid():
                section = form.save(commit=False)
                section.course = course
                section.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'add_content' in request.POST:
            form2 = ContentCreateForm(request.POST, request.FILES)
            if form2.is_valid():
                content = form2.save(commit=False)
                section_id = int(request.POST.get('section_name'))
                current_section = Section.objects.get(id=section_id)
                content.section = current_section
                content.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'course': course,
        'sections': sections,
        'form': form,
        'form2': form2,
    }
    return render(request, 'admin_panel/bcsTF/courseDetail.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminCourseContentDelete(request, id):
    current_content = Content.objects.get(id=id)
    current_content.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminCourseContentEdit(request, id):
    current_content = Content.objects.get(id=id)
    form = ContentCreateForm(instance=current_content)
    if request.method == 'POST':
        form = ContentCreateForm(request.POST, request.FILES, instance=current_content)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminCourseSectionEdit(request, id):
    current_section = Section.objects.get(id=id)
    form = SectionCreateForm(instance=current_section)
    if request.method == 'POST':
        form = SectionCreateForm(request.POST, request.FILES, instance=current_section)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminOrdersView(request):
    orders = models.Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'admin_panel/bcsTF/orders.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminOrdersDetailView(request):
    return render(request, 'admin_panel/bcsTF/order_detail.html')


# bcs academy user panel
@login_required
def UserCourses(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        courses = Course.objects.filter(course_type='Business')
        context = {
            'courses': courses,
        }

        return render(request, "user_panel/academy/courses.html", context)


@login_required
def myCourses(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        courses = Course.objects.filter(course_type='Business')

        context = {
            'courses': courses,
        }

        return render(request, "user_panel/academy/mycourses.html", context)


@login_required
def UserCoursesDetails(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            course = Course.objects.get(id=id, course_type='Business')

            context = {
                'course': course,
            }

            return render(request, "user_panel/academy/details.html", context)
        except:
            return HttpResponse('You are not authorized to view this page')


@login_required
def UserFiles(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            course = Course.objects.get(id=id, course_type='Business')
            # section = Section.objects.filter(course=course)
            contents = Content.objects.filter(section__course=course)
            paginator = Paginator(contents, 1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'course': course,
                'contents': contents,
                'content_type': 'instruction',
                'section_no': 1,
                'module_no': 1,
                'page_obj': page_obj
            }

            return render(request, "user_panel/academy/files.html", context)
        except:
            return HttpResponse('You are not authorized to view this page')
