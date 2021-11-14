from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from Account import models, forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


# @login_executed('account_app:profile')
# def signupView(request):
#     form = forms.RegistrationForm()
#     if request.method == 'POST':
#         form = forms.RegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return HttpResponseRedirect(reverse('account_app:profile'))
#     context = {
#         'form': form,
#     }
#     return render(request, 'account/signup.html', context)
#
#
# @login_executed('account_app:profile')
# def loginView(request):
#     form = forms.LoginForm()
#     next_url = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(data=request.POST)
#         username, password = request.POST.get('username'), request.POST.get('password')
#         next_url = request.GET.get('next')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return HttpResponseRedirect(reverse('account_app:profile'))
#     context = {
#         'form': form,
#     }
#     return render(request, 'account/login.html', context)

@login_required
def profileView(request):
    current_user = request.user
    interests = models.Interest.objects.get(user=current_user)
    form = forms.InterestForm(instance=interests)
    if not current_user.phone_number \
            or not current_user.country \
            or not current_user.phone_number \
            or not current_user.birth_date \
            or not current_user.gender:

        emails = current_user.emailaddress_set.all
        if not current_user.phone_number \
                or not current_user.country:
            form = forms.CountryPhoneForm(instance=current_user)
            message = 'Add Country and Phone Number'
            if request.POST:
                form = forms.CountryPhoneForm(request.POST, instance=current_user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif not current_user.birth_date \
                or not current_user.gender:
            form = forms.BirthDateGenderForm(instance=current_user)
            message = 'Add Date of Birth and Gender'
            if request.POST:
                form = forms.BirthDateGenderForm(request.POST, instance=current_user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        context = {
            'emails': emails,
            'form': form,
            'message': message,
        }
        return render(request, 'account/profile-info-add.html', context)
    else:
        if request.method == 'POST':
            form = forms.InterestForm(request.POST, instance=interests)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        context = {
            # 'interests': interests,
            'form': form,
        }
        return render(request, 'account/profile.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


@login_required
def profileInfoAddView(request):
    current_user = request.user
    emails = current_user.emailaddress_set.all

    context = {
        'emails': emails,

    }
    return render(request, 'account/profile-info-add.html', context)
