from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from Academy.models import Course, Section, Content
from Academy.forms import CourseCreateForm, SectionCreateForm, ContentCreateForm
from django.core.paginator import Paginator
from BusinessSecurity.models import Events, RegisteredEvents


# Create your views here.
def superuser_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


def pcs_admin_permission_check(user):
    try:
        return user.is_superuser or ((
                                             user.permission_user.is_superadmin or user.permission_user.is_admin or user.permission_user.is_moderator or user.permission_user.is_editor) and (
                                             user.permission_user.admin_type == 'pcs_admin' or user.permission_user.admin_type == 'main_admin'))
    except:
        return user.is_superuser


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
    context = {

    }
    return render(request, 'user_panel/pcs/ticket.html', context)


@login_required
def userDashboardView(request):
    events = Events.objects.filter(status='active')
    registered_event = RegisteredEvents.objects.filter(user=request.user).values_list('event', flat=True)

    context = {
        'events': events,
        'registered_event': registered_event,
    }
    return render(request, 'user_panel/pcs/dashboard.html', context)


@login_required
def userServicesView(request):
    courses = Course.objects.filter(course_type='Personal')
    context = {
        'courses': courses,
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


# bcs academy user panel
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
    return render(request, 'admin_panel/pcsTF/dashboard.html')


def pcsAdminService(request):
    return render(request, 'admin_panel/pcsTF/service.html')


def pcsAdminSubService(request):
    return render(request, 'admin_panel/pcsTF/subService.html')


def pcsAdminSubscriptionList(request):
    return render(request, 'admin_panel/pcsTF/subscriptionList.html')


def pcsAdminSubscriptionPack(request):
    return render(request, 'admin_panel/pcsTF/subscriptionPack.html')


def pcsAdminReadingList(request):
    return render(request, 'admin_panel/pcsTF/readingList.html')


def pcsAdminRevenue(request):
    return render(request, 'admin_panel/pcsTF/revenue.html')


def pcsAdminIndividualUser(request):
    return render(request, 'admin_panel/pcsTF/users.html')


def pcsAdminIndividualUserPanel(request):
    return render(request, 'admin_panel/pcsTF/userPanel.html')


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
def pcsAdminTraining(request):
    form = CourseCreateForm()
    courses = Course.objects.filter(course_type='Personal')
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
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
    form = CourseCreateForm(instance=current_course)

    if request.method == 'POST':
        form = CourseCreateForm(request.POST, instance=current_course)
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
