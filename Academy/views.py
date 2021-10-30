from django.shortcuts import render
from Academy import models


# Create your views here.

def academyHomeView(request):
    context = {

    }

    return render(request, 'academypages/index.html', context)


def ccspView(request):
    context = {

    }

    return render(request, 'academypages/pages/ccsp.html', context)


def academyFAQView(request):
    context = {

    }

    return render(request, 'academypages/pages/academy_faq.html', context)


def corporateTrainingView(request):
    context = {

    }

    return render(request, 'academypages/pages/corporate_training.html', context)


def lawEnforcementView(request):
    context = {

    }

    return render(request, 'academypages/pages/law_enforcement.html', context)


def educationalInstituteView(request):
    context = {

    }

    return render(request, 'academypages/pages/educational_institute.html', context)


# user panel
def UserCourses(request):
    courses = models.Course.objects.all()
    context = {
        'courses': courses,
    }

    return render(request, "user_panel/academy/courses.html", context)


def myCourses(request):

    courses = models.Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, "user_panel/academy/mycourses.html", context)

def UserCoursesDetails(request, id):
    course = models.Course.objects.get(id=id)

    context = {
        'course': course,
    }

    return render(request, "user_panel/academy/details.html", context)


def UserFiles(request, id):
    course = models.Course.objects.get(id=id)
    context = {
        'course': course,
        'content_type': 'instruction',
        'section_no': 1,
        'module_no': 1
    }

    return render(request, "user_panel/academy/files.html", context)


# to get specific course material
def course_material(request, section, module, content_type):
    template_name = "user_panel/academy/files.html"

    section_no = int(section.split('-')[1])
    module_no = int(module.split('-')[1])

    section_no = 1 if section_no == 0 else section_no
    module_no = 1 if module_no == 0 else module_no

    if module_no > 3:
        section_no += 1
        module_no = 1

    content_type = 'instruction' if content_type == 'video' else 'video'

    print(section_no, module_no, content_type)
    return render(request, template_name,
                  {'content_type': content_type, 'section_no': section_no, 'module_no': module_no})


def UserExams(request):
    template_name = "user_panel/academy/exams.html"

    return render(request, template_name)


def UserEvents(request):
    template_name = "user_panel/academy/events.html"

    return render(request, template_name)


def UserNotifications(request):
    template_name = "user_panel/academy/notifications.html"

    return render(request, template_name)


def UserSettings(request):
    template_name = "user_panel/academy/settings.html"

    return render(request, template_name)


# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


# this function is to control the downloading system for pdf's.
def download_file(request, path=''):
    file_name = path
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/media/' + path
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % file_name
        return response
    except:
        return HttpResponse('File not found on the server.')
