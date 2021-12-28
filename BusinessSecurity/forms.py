from django import forms
from BusinessSecurity import models
# from Academy.models import Course, duration, Section, Content
from django.db.models import Q
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class AddServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        # fields = '__all__'
        exclude = ['category_choice', ]


class AddServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='bcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Service
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body',
                  'service_footer', ]


class AddSubscriptionServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='bcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.SubscriptionServices
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body',
                  'service_footer', ]





class AddForm(forms.ModelForm):
    class Meta:
        model = models.InputFields
        fields = '__all__'


class AddSubServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=models.Service.objects.filter(has_sub_service=True, category_choice='bcs'),
        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.SubService
        fields = '__all__'
        exclude = ['total_customer', ]
        widgets = {
            'fields': forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'})
        }


class CreateBusinessForm(forms.ModelForm):
    position = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Designation'}))
    website = forms.URLField(widget=forms.URLInput(
        attrs={'pattern': "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
               'value': "https://"}))

    class Meta:
        model = models.Business
        fields = '__all__'
        exclude = ['unique_id', 'company_logo']


class AddPackageForm(forms.ModelForm):
    service_id = forms.ModelChoiceField(
        queryset=models.SubscriptionServices.objects.filter(category_choice='bcs'))

    class Meta:
        model = models.SubscriptionBasedPackage
        fields = '__all__'
        exclude = ['package_id']


class AddPackageFeatureForm(forms.ModelForm):
    # service_id = forms.ModelChoiceField(queryset=models.Service.objects.filter(is_subscription_based=True))

    class Meta:
        model = models.SubscriptionFeatures
        fields = '__all__'


class AddIndividualPackageFeatureForm(forms.ModelForm):
    class Meta:
        model = models.SubscriptionFeatures
        fields = ['feature_name', 'feature']


class EventCreateForm(forms.ModelForm):
    date_field = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'time'}),
                                     input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])

    class Meta:
        model = models.Events
        fields = '__all__'


class OrderPriceForm(forms.ModelForm):
    class Meta:
        model = models.OrderPrice
        fields = ['price', 'currency', 'payment_method']
        widgets = {
            'currency': forms.Select(attrs={'class': 'form-select'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'})
        }


class OrderAssignForm(forms.ModelForm):
    staff = forms.ModelChoiceField(
        queryset=models.User.objects.filter(
            Q(is_staff=True, is_sales=True) | Q(is_superuser=True) | Q(is_staff=True, is_sales_head=True)),
        widget=forms.Select(attrs={'class': 'js-example-basic-single form-control form-select'}))

    class Meta:
        model = models.OrderStaff
        fields = ['staff', ]


class TicketCreateForm(forms.ModelForm):
    ticket_category = forms.Field(
        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.Ticket
        fields = ['ticket_title', 'ticket_category',
                  'ticket_description', 'ticket_attachment']
        # exclude = ['category_choice', 'ticket_status']


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = models.TicketComment
        fields = ['comment']


class BusinessLogoForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = ['company_logo']


class BusinessInfoForm(forms.ModelForm):
    # industry_type = forms.Field(widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = models.Business
        exclude = ['company_logo', 'unique_id']
        widgets = {
            'industry_type': forms.Select(attrs={'class': 'form-select'})
        }


class AssignToServiceForm(forms.ModelForm):
    class Meta:
        model = models.ServiceAssigned
        fields = ['service']
        widgets = {
            'service': forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple'})
        }


class NotificationForm(forms.ModelForm):
    category_choice = forms.ChoiceField(label='Select Target Users', choices=models.category_choice)
    notification = forms.Field(widget=forms.Textarea(attrs={'cols': '10', 'rows': '5'}))

    class Meta:
        model = models.Notification
        fields = '__all__'
