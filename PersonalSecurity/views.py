from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from Academy.models import Course, Section, Content, CourseCategory
from Academy.forms import PCSCourseCreateForm, SectionCreateForm, ContentCreateForm, CourseCategoryCreateForm
from django.core.paginator import Paginator
from BusinessSecurity import models, forms
from PersonalSecurity import forms as pcsforms
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from Blog.models import ReadingList


# Create your views here.
def superuser_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


def pcs_admin_permission_check(user):
    try:
        return user.is_staff and user.is_superuser or user.is_pcs_head
    except:
        return user.is_staff and user.is_superuser


def pcs_admin_permission_check_order(user):
    try:
        return user.is_staff and user.is_superuser or user.is_pcs_head or user.is_sales
    except:
        return user.is_staff and user.is_superuser


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


def openTicketView(request):
    form = forms.TicketCreateForm()
    tickets = models.Ticket.objects.filter(user=request.user, category_choice='pcs').order_by('-ticket_date')
    if request.method == 'POST':
        form = forms.TicketCreateForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.category_choice = 'pcs'
            ticket.ticket_status = 'open'
            ticket.ticket_category = request.POST.get('ticket_category')
            ticket.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'tickets': tickets,
    }
    return render(request, 'user_panel/pcs/ticket.html', context)


def ticketDetailView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/ticket_detail.html', context)


@login_required
def userDashboardView(request):
    events = models.Events.objects.filter(status='active', category='for_personal_security')
    registered_event = models.RegisteredEvents.objects.filter(user=request.user).values_list('event', flat=True)
    orders = models.Order.objects.filter(
        Q(user=request.user, category_choice='pcs') & ~Q(Q(order_status='new') | Q(order_status='attending'))).order_by(
        '-order_date')[:2]
    context = {
        'events': events,
        'registered_event': registered_event,
        'orders': orders,
    }
    return render(request, 'user_panel/pcs/dashboard.html', context)


@login_required
def userReadingListView(request):
    readinglists = ReadingList.objects.filter(user=request.user)

    context = {
        'readinglists': readinglists
    }
    return render(request, 'user_panel/pcs/reading_list.html', context)


@login_required
def userServicesView(request):
    courses = Course.objects.filter(course_type='Personal')
    courses_categories = CourseCategory.objects.filter(course_type='Personal')
    service_category = models.ServiceCategory.objects.filter(category_choice='pcs')
    services = models.Service.objects.filter(category_choice='pcs')
    subscription_services = models.SubscriptionServices.objects.filter(category_choice='pcs')
    if request.method == 'POST':
        data_list = request.POST
        file_list = request.FILES
        # print(data_list)
        # print(file_list)

        current_service = get_object_or_404(models.Service, service_title=data_list['service_name'],
                                            category_choice='pcs')

        for data in data_list:
            if data != 'csrfmiddlewaretoken' and data != 'service_name':
                current_input = models.SubServiceInput.objects.get(id=data)
                input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                        inputinfo=data_list[data])
                input_data.save()
                order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                           service=current_service, category_choice='pcs')

                order[0].subserviceinput.add(input_data)
        for files in file_list:
            current_input = models.SubServiceInput.objects.get(id=files)
            myfile = file_list[files]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                    inputinfo=uploaded_file_url)
            input_data.save()
            order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                       service=current_service, category_choice='pcs')

            order[0].subserviceinput.add(input_data)

        order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                   service=current_service, category_choice='pcs')

        if not order[0].orderstaff_order.all().exists():
            tracking = models.Tracking.objects.get(service=current_service)
            persons = tracking.persons
            persons_list = list(filter(None, persons.split(',')))
            person = persons_list.pop(0)
            persons_list.append(person)
            tracking.persons = ','.join(persons_list)
            tracking.save()
            current_staff = models.User.objects.get(id=person)
            order_staff = models.OrderStaff.objects.create(staff=current_staff, order=order[0])
            order_staff.save()
        return render(request, 'user_panel/pcs/thanks.html')
    context = {
        'service_category': service_category,
        'services': services,
        'services_headings': list(services.values_list('service_title', flat=True)),
        'subscription_services': subscription_services,
        'subscription_services_headings': list(subscription_services.values_list('service_title', flat=True)),
        'courses_categories': courses_categories,
        'courses': courses,
        'courses_headings': list(courses.values_list('course_name', flat=True)),
    }
    return render(request, 'user_panel/pcs/services.html', context)


@login_required
def userQuotationsHistoryView(request):
    orders = models.Order.objects.filter(
        Q(user=request.user, category_choice='pcs') & Q(
            Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
        '-order_date')
    context = {
        'orders': orders,
        'message': 'Quotations',
    }
    return render(request, 'user_panel/pcs/order_history.html', context)


@login_required
def userOrderHistoryView(request):
    orders = models.Order.objects.filter(
        Q(user=request.user, category_choice='pcs') & ~Q(
            Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
        '-order_date')
    context = {
        'orders': orders,
        'message': 'Orders',
    }
    return render(request, 'user_panel/pcs/order_history.html', context)


@login_required
def userOrderDetailsView(request, id):
    try:
        current_order = models.Order.objects.get(user=request.user, id=id, category_choice='pcs')
        context = {
            'current_order': current_order,
        }
        return render(request, 'user_panel/pcs/order_detail.html', context)
    except:
        return HttpResponse("You don't have permission to view this page")


@login_required
def userSubscriptionsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    registered_event = models.RegisteredEvents.objects.filter(user=request.user).values_list('event', flat=True)
    events = models.Events.objects.filter(category='for_personal_security',
                                          registered_event_event__user=request.user)
    context = {
        'events': events,
        'registered_event': registered_event,
    }
    return render(request, 'user_panel/pcs/events.html', context)


@login_required
def userNotificationsView(request):
    notifications = models.Notification.objects.filter(category_choice='pcs').order_by('-notification_time')
    context = {
        'notifications': notifications
    }
    return render(request, 'user_panel/pcs/notifications.html', context)


@login_required
def userSettingsView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/settings.html', context)


@login_required
def pcsAppointmentView(request):
    context = {

    }
    return render(request, 'user_panel/pcs/appoinment.html', context)


# pcs academy user panel
@login_required
def UserCourses(request):
    courses = Course.objects.filter(course_type='Personal')
    context = {
        'courses': courses,
    }

    return render(request, "user_panel/academy/courses.html", context)


@login_required
def myCourses(request):
    courses = Course.objects.filter(course_type='Personal')

    context = {
        'courses': courses,
    }

    return render(request, "user_panel/academy/mycourses.html", context)


@login_required
def UserCoursesDetails(request, id):
    try:
        course = Course.objects.get(id=id, course_type='Personal')

        context = {
            'course': course,
        }

        return render(request, "user_panel/academy/details.html", context)
    except:
        return HttpResponse('You are not authorized to view this page')


@login_required
def UserFiles(request, id):
    try:
        course = Course.objects.get(id=id, course_type='Personal')
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


# New

#    pcs admin views

def pcsAdminDashboard(request):
    service_categories = models.ServiceCategory.objects.filter(category_choice='pcs')

    context = {
        'service_categories': service_categories
    }
    return render(request, 'admin_panel/pcsTF/dashboard.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceCategoryView(request):
    categories = models.ServiceCategory.objects.filter(category_choice='pcs')
    form = forms.AddServiceCategoryForm()
    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.category_choice = 'pcs'
            category.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'admin_panel/pcsTF/serviceCategory.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceCategoryDeleteView(request, id):
    current_category = models.ServiceCategory.objects.get(id=id, category_choice='pcs')
    current_category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceCategoryEditView(request, id):
    current_category = models.ServiceCategory.objects.get(id=id, category_choice='pcs')
    form = forms.AddServiceCategoryForm(instance=current_category)

    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(request.POST, instance=current_category)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('pcs_admin_services_category'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceView(request):
    form = pcsforms.AddServiceForm()
    sales_persons = models.User.objects.filter(Q(is_staff=True, is_sales=True))
    services = models.Service.objects.filter(category_choice='pcs')
    if request.method == 'POST':
        form = pcsforms.AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.category_choice = 'pcs'
            service.save()
            for sale_id in request.POST.getlist('sales'):
                current_sales = models.User.objects.get(id=sale_id)
                current_assigned = models.ServiceAssigned.objects.get_or_create(user=current_sales)
                current_assigned[0].service.add(service)
                current_assigned[0].save()
                tracking = models.Tracking.objects.get_or_create(service=service)
                person = tracking[0].persons
                tracking[0].persons = f'{person},{sale_id}'
                tracking[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'sales_persons': sales_persons,
        'services': services,
    }
    return render(request, 'admin_panel/pcsTF/service.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubscriptionServiceView(request):
    form = pcsforms.AddSubscriptionServiceForm()
    # sales_persons = models.User.objects.filter(Q(is_staff=True, is_sales=True))
    services = models.SubscriptionServices.objects.filter(category_choice='pcs')

    if request.method == 'POST':
        form = pcsforms.AddSubscriptionServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.category_choice = 'pcs'
            service.save()
            # for sale_id in request.POST.getlist('sales'):
            #     current_sales = models.User.objects.get(id=sale_id)
            #     current_assigned = models.ServiceAssigned.objects.get_or_create(user=current_sales)
            #     current_assigned[0].service.add(service)
            #     current_assigned[0].save()
            #     tracking = models.Tracking.objects.get_or_create(service=service)
            #     person = tracking[0].persons
            #     tracking[0].persons = f'{person},{sale_id}'
            #     tracking[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        # 'sales_persons': sales_persons,
        'services': services,
    }
    return render(request, 'admin_panel/pcsTF/subscription-service.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceDeleteView(request, id):
    current_service = models.Service.objects.get(id=id)
    current_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubscriptionServiceEditView(request, id):
    current_service = models.SubscriptionServices.objects.get(id=id)
    form = pcsforms.AddSubscriptionServiceForm(instance=current_service)

    if request.method == 'POST':
        form = pcsforms.AddSubscriptionServiceForm(request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('pcs_admin_subscription_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminServiceEditView(request, id):
    current_service = models.Service.objects.get(id=id)
    form = pcsforms.AddServiceForm(instance=current_service)

    if request.method == 'POST':
        form = pcsforms.AddServiceForm(request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('pcs_admin_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsSubServiceFormView(request):
    form = forms.AddForm()
    form_lists = models.InputFields.objects.all()
    select_choices = list(models.SelectChoice.objects.all().values('id', 'choices'))

    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            current_input = form.save()
            current_input_field = models.InputFields.objects.get(id=current_input.id)
            if request.POST.getlist('options'):
                for i in request.POST.getlist('options'):
                    field = models.SelectChoice.objects.get(id=i)
                    new_choices = models.SelectChoiceRelation.objects.get_or_create(input_field=current_input_field)
                    new_choices[0].choice_field.add(field)
                    new_choices[0].save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'form_lists': form_lists,
        'select_choices': select_choices,
    }
    return render(request, 'admin_panel/pcsTF/subserviceForms.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubServiceFormDeleteView(request, id):
    input_field = models.InputFields.objects.get(id=id)
    input_field.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubServiceFormEditView(request, id):
    current_input_field = models.InputFields.objects.get(id=id)
    form = forms.AddForm(instance=current_input_field)

    if request.method == 'POST':
        form = forms.AddForm(request.POST, instance=current_input_field)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('pcs_admin_sub_services_form'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


# Not worked from here
@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubServiceView(request):
    form = pcsforms.AddSubServiceForm()
    sub_services = models.SubService.objects.filter(service__category_choice='pcs')
    if request.method == 'POST':
        form = pcsforms.AddSubServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'sub_services': sub_services,
    }
    return render(request, 'admin_panel/pcsTF/subService.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubServiceDeleteView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    current_sub_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubServiceEditView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    form = pcsforms.AddSubServiceForm(instance=current_sub_service)

    if request.method == 'POST':
        form = pcsforms.AddSubServiceForm(request.POST, instance=current_sub_service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pcs_admin_sub_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


def pcsAdminSubService(request):
    return render(request, 'admin_panel/pcsTF/subService.html')


def pcsAdminSubscriptionList(request):
    return render(request, 'admin_panel/pcsTF/subscriptionList.html')


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminSubscriptionPack(request):
    form = pcsforms.AddPackageForm()
    services = models.SubscriptionServices.objects.filter(category_choice='pcs')

    if request.method == 'POST':
        feature_names = request.POST.getlist('featureName')
        features = request.POST.getlist('feature')
        form = pcsforms.AddPackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)

            package.save()
            for feature_name, feature in zip(feature_names, features):
                package_feature = models.SubscriptionFeatures.objects.get_or_create(package=package,
                                                                                    feature_name=feature_name,
                                                                                    feature=feature)
                package_feature[0].save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'services': services,
    }
    return render(request, 'admin_panel/pcsTF/subscriptionPack.html', context)


def pcsAdminReadingList(request):
    return render(request, 'admin_panel/pcsTF/readingList.html')


def pcsAdminRevenue(request):
    return render(request, 'admin_panel/pcsTF/revenue.html')


def pcsAdminIndividualUser(request):
    all_users = models.User.objects.filter(Q(is_superuser=False))
    context = {
        'all_users': all_users,
    }
    return render(request, 'admin_panel/pcsTF/users.html', context)


def pcsAdminIndividualUserPanel(request, id):
    current_user = models.User.objects.get(id=id)
    orders = models.Order.objects.filter(user=current_user, category_choice='pcs')

    context = {
        'current_user': current_user,
        'orders': orders,
    }
    return render(request, 'admin_panel/pcsTF/userPanel.html', context)


def pcsAdminList(request):
    return render(request, 'admin_panel/pcsTF/adminUsers.html')


def pcsAdminProfile(request):
    return render(request, 'admin_panel/pcsTF/myProfile.html')


def pcsAdminUserInterest(request):
    return render(request, 'admin_panel/pcsTF/userInterest.html')


def pcsAdminTraining(request):
    return render(request, 'admin_panel/pcsTF/training.html')


def pcsAdminCourseDetail(request):
    return render(request, 'admin_panel/pcsTF/courseDetail.html')


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTrainingCategoryView(request):
    form = CourseCategoryCreateForm()
    categories = CourseCategory.objects.filter(course_type='Personal')
    if request.method == 'POST':
        form = CourseCategoryCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_type = 'Personal'
            course.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'admin_panel/pcsTF/trainingCategory.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTrainingCategoryEditView(request, id):
    current_category = CourseCategory.objects.get(id=id)
    form = CourseCategoryCreateForm(instance=current_category)
    if request.method == 'POST':
        form = CourseCategoryCreateForm(request.POST, instance=current_category)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')

            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('pcs_admin_training_category'))
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTrainingCategoryDelete(request, id):
    current_category = CourseCategory.objects.get(id=id)
    current_category.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTraining(request):
    form = PCSCourseCreateForm()
    courses = Course.objects.filter(course_type='Personal')
    if request.method == 'POST':
        form = PCSCourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_type = 'Personal'
            course.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'courses': courses,
    }
    return render(request, 'admin_panel/pcsTF/training.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTrainingDelete(request, id):
    current_course = Course.objects.get(id=id)
    current_course.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminTrainingEdit(request, id):
    current_course = Course.objects.get(id=id)
    form = PCSCourseCreateForm(instance=current_course)

    if request.method == 'POST':
        form = PCSCourseCreateForm(request.POST, instance=current_course)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('pcs_admin_training'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminCourseDetail(request, id):
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
    return render(request, 'admin_panel/pcsTF/courseDetail.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminCourseContentDelete(request, id):
    current_content = Content.objects.get(id=id)
    current_content.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminCourseContentEdit(request, id):
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
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/')
def pcsAdminCourseSectionEdit(request, id):
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
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminQuotationsView(request):
    if request.user.is_sales:
        orders = models.Order.objects.filter(
            Q(orderstaff_order__staff=request.user) & Q(Q(order_status='new') | Q(order_status='attending')
                                                        | Q(order_status='assigned'))).order_by('-order_date')
        context = {
            'orders': orders,
            'message': 'Quotations',
        }
        return render(request, 'admin_panel/pcsTF/orders.html', context)
    else:
        orders = models.Order.objects.filter(
            Q(category_choice='pcs') & Q(Q(order_status='new') | Q(order_status='attending')
                                         | Q(order_status='assigned'))).order_by('-order_date')
        print(orders)
        context = {
            'orders': orders,
            'message': 'Quotations',
            'admin': 'admin',
        }
        return render(request, 'admin_panel/pcsTF/orders.html', context)


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrdersView(request):
    if request.user.is_sales:
        orders = models.Order.objects.filter(
            Q(orderstaff_order__staff=request.user) & ~Q(
                Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
            '-order_date')
        context = {
            'orders': orders,
            'message': 'Orders',
        }
        return render(request, 'admin_panel/pcsTF/orders.html', context)
    else:
        orders = models.Order.objects.filter(
            Q(category_choice='pcs') & ~Q(
                Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
            '-order_date')
        context = {
            'orders': orders,
            'message': 'Orders',
        }
        return render(request, 'admin_panel/pcsTF/orders.html', context)


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminNewOrdersView(request):
    service_category = models.ServiceCategory.objects.filter(category_choice='pcs',
                                                             service_category__service_assigned_service__user=request.user)
    user_lists = models.User.objects.all()
    services = models.Service.objects.filter(category_choice='pcs', service_assigned_service__user=request.user)

    # print(service_category.count())
    # print(services.count())
    if request.method == 'POST':
        data_list = request.POST
        file_list = request.FILES
        current_customer = models.User.objects.get(email=data_list.get('customer'))
        # print(current_customer)
        # print(data_list)
        # print(file_list)

        current_service = get_object_or_404(models.Service, service_title=data_list['service_name'])

        for data in data_list:
            if data != 'csrfmiddlewaretoken' and data != 'service_name' and data != 'customer':
                current_input = models.SubServiceInput.objects.get(id=data)
                input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                        inputinfo=data_list[data])
                input_data.save()
                order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                           service=current_service, category_choice='pcs')

                order[0].subserviceinput.add(input_data)
        for files in file_list:
            current_input = models.SubServiceInput.objects.get(id=files)
            myfile = file_list[files]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                    inputinfo=uploaded_file_url)
            input_data.save()
            order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                       service=current_service, category_choice='pcs')

            order[0].subserviceinput.add(input_data)

        order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                   service=current_service, category_choice='pcs')
        print(order)
        order_staff = models.OrderStaff.objects.get_or_create(staff=request.user, order=order[0])
        order_staff[0].save()
        return HttpResponseRedirect(reverse('pcs_admin_quotations'))
    context = {
        'service_category': service_category,
        'services': services,
        'user_lists': user_lists,
        'services_headings': list(services.values_list('service_title', flat=True)),
    }
    return render(request, 'admin_panel/pcsTF/create_user_services.html', context)


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrdersDetailView(request, id):
    if request.user.is_superuser or request.user.is_pcs_head:
        current_order = models.Order.objects.get(id=id)
        current_price = models.OrderPrice.objects.get(order=current_order)
        form = forms.OrderPriceForm(instance=current_price)
        if request.method == 'POST':
            form = forms.OrderPriceForm(request.POST, instance=current_price)
            if form.is_valid():
                current_order.order_status = 'on_progress'
                current_order.save()
                # new_staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
                form.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        context = {
            'current_order': current_order,
            'form': form,
        }
        return render(request, 'admin_panel/pcsTF/order_detail.html', context)
    else:
        try:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user)
            form = forms.OrderPriceForm(instance=current_order)
            if request.method == 'POST':
                form = forms.OrderPriceForm(request.POST, instance=current_order)
                if form.is_valid():
                    current_order.order_status = 'on_progress'
                    # new_staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
                    form.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            context = {
                'current_order': current_order,
                'form': form,
            }
            return render(request, 'admin_panel/pcsTF/order_detail.html', context)
        except:
            return HttpResponse("You don't have permission to view this page!")


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrderNewView(request, id):
    # print(request.user.is_staff)
    try:
        # current_order = models.Order.objects.get(
        #     Q(id=id, orderstaff_order__staff=request.user, orderstaff_order__staff__is_staff=True,
        #       orderstaff_order__staff__is_sales_head=True) | Q(id=id, orderstaff_order__staff__is_superuser=True) | Q(
        #         id=id, orderstaff_order__staff__is_staff=True, orderstaff_order__staff__is_sales_head=True))
        if request.user.is_superuser or request.user.is_pcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)
        # print(request.user.is_pcs_head)
        current_order.order_status = 'new'
        current_order.price = 0
        # if current_order.orderstaff_order.exists():
        #     for staff in current_order.orderstaff_order.all():
        #         staff.delete()
        current_order.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrderAttendingView(request, id):
    try:
        if request.user.is_superuser or request.user.is_pcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'attending'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrderCompletedView(request, id):
    try:
        if request.user.is_superuser or request.user.is_pcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'completed'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def pcsAdminOrderCanceledView(request, id):
    try:
        if request.user.is_superuser or request.user.is_pcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'canceled'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminTicketsView(request):
    tickets = models.Ticket.objects.filter(category_choice='pcs')
    context = {
        'tickets': tickets,
    }
    return render(request, 'admin_panel/pcsTF/allTickets.html', context)


@user_passes_test(pcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def pcsAdminTicketsDetailView(request, id):
    ticket = models.Ticket.objects.get(id=id)
    commentform = forms.TicketCommentForm()
    if request.method == 'POST':
        commentform = forms.TicketCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'ticket': ticket,
        'commentform': commentform,
    }
    return render(request, 'admin_panel/pcsTF/ticket_detail.html', context)
