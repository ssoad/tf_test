from django import forms
from Account import models
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
)
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

from allauth.account.forms import LoginForm as LF


class RegistrationForm(UserCreationForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'style': ' border: 1px '
                                                                                   'solid #000;border-radius: '
                                                                                   '0;outline: 0;padding-left: '
                                                                                   '5px;height: 35px;'}))

    country = CountryField().formfield(widget=CountrySelectWidget(attrs={'style': ' border: 1px '
                                                                                  'solid #000;border-radius: '
                                                                                  '0;outline: 0;padding-left: '
                                                                                  '5px;height: 35px;'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                                             'solid #000;border-radius: '
                                                                                             '0;outline: 0;padding-left: '
                                                                                             '5px;height: 35px;'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                                                     'solid #000;border-radius: '
                                                                                                     '0;outline: 0;padding-left: '
                                                                                                     '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'country', 'birth_date', 'gender', 'profile_pic',
                  'password1',
                  'password2', 'newsletter']
        widgets = {
            'gender': forms.Select(attrs={'style': ' border: 1px '
                                                   'solid #000;border-radius: '
                                                   '0;outline: 0;padding-left: '
                                                   '5px;height: 35px;'}),
            'first_name': forms.TextInput(attrs={'style': ' border: 1px '
                                                          'solid #000;border-radius: '
                                                          '0;outline: 0;padding-left: '
                                                          '5px;height: 35px;'}),
            'last_name': forms.TextInput(attrs={'style': ' border: 1px '
                                                         'solid #000;border-radius: '
                                                         '0;outline: 0;padding-left: '
                                                         '5px;height: 35px;'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'style': ' border: 1px '
                                                                          'solid #000;border-radius: '
                                                                          '0;outline: 0;padding-left: '
                                                                          '5px;height: 35px;'}),
            'email': forms.EmailInput(attrs={'style': ' border: 1px '
                                                      'solid #000;border-radius: '
                                                      '0;outline: 0;padding-left: '
                                                      '5px;height: 35px;'}),
            'profile_pic': forms.FileInput(attrs={'style': ' border: 1px '
                                                           'solid #000;border-radius: '
                                                           '0;outline: 0;padding-left: '
                                                           '5px;height: 35px;'}),
            # 'newsletter': forms.CheckboxInput(attrs={'style': ''})

        }


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'style': ' border: 1px '
                                                                        'solid #000;border-radius: '
                                                                        '0;outline: 0;padding-left: '
                                                                        '5px;height: 35px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                          'solid #000;border-radius: '
                                                                          '0;outline: 0;padding-left: '
                                                                          '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = '__all__'


class LoginForm2(LF):
    # username = forms.EmailField(widget=forms.EmailInput(attrs={'style': ' border: 1px '
    #                                                                     'solid #000;border-radius: '
    #                                                                     '0;outline: 0;padding-left: '
    #                                                                     '5px;height: 35px;'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'style': ' border: 1px '
    #                                                                       'solid #000;border-radius: '
    #                                                                       '0;outline: 0;padding-left: '
    #                                                                       '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = '__all__'


class SelectPermissionForm(forms.ModelForm):
    class Meta:
        model = models.Permissions
        fields = '__all__'
        exclude = ['user', ]
