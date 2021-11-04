from django import forms
from BusinessSecurity import models
from Academy.models import Course, duration, Section, Content


class AddServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        fields = '__all__'


class AddServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.all())

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Service
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'has_sub_service',
                  'is_subscription_based', 'service_header', 'service_body', 'service_footer', ]


class AddForm(forms.ModelForm):
    class Meta:
        model = models.InputFields
        fields = '__all__'


class AddSubServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=models.Service.objects.filter(has_sub_service=True),
                                     widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.SubService
        fields = '__all__'
        exclude = ['total_customer', ]


class CreateBusinessForm(forms.ModelForm):
    position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CEO'}))

    class Meta:
        model = models.Business
        fields = '__all__'
        exclude = ['unique_id', ]


class AddPackageForm(forms.ModelForm):
    service_id = forms.ModelChoiceField(queryset=models.Service.objects.filter(is_subscription_based=True))

    class Meta:
        model = models.SubscriptionBasedPackage
        fields = '__all__'


class AddPackageFeatureForm(forms.ModelForm):
    # service_id = forms.ModelChoiceField(queryset=models.Service.objects.filter(is_subscription_based=True))

    class Meta:
        model = models.SubscriptionFeatures
        fields = '__all__'


class AddIndividualPackageFeatureForm(forms.ModelForm):
    class Meta:
        model = models.SubscriptionFeatures
        fields = ['feature_name', ]


class EventCreateForm(forms.ModelForm):
    date_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'time'}),
                                     input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])

    class Meta:
        model = models.Events
        fields = '__all__'


class OrderPriceForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['price', ]


class OrderAssignForm(forms.ModelForm):
    # staff = forms.ModelChoiceField(queryset=models.User.objects.filter(is_staff=True, is_sales=True), widget=forms.Select(attrs={'class': 'js-example-basic-single form-control form-select'}))

    class Meta:
        model = models.OrderStaff
        fields = ['staff', ]


class TicketCreateForm(forms.ModelForm):

    class Meta:
        model = models.Ticket
        fields = ['ticket_title', 'ticket_category', 'ticket_description', 'ticket_attachment']
        # exclude = ['ticket_type', 'ticket_status']
