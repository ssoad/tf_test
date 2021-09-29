from django.shortcuts import render


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


import mimetypes
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
