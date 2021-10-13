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
    context = {

    }
    return render(request, 'account/profile.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
