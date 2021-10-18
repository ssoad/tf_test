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


class AddSubServiceForm(forms.ModelForm):
    sub_service = forms.ModelChoiceField(queryset=models.Service.objects.filter(has_sub_service=True),
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


class CourseCreateForm(forms.ModelForm):
    duration = forms.ChoiceField(choices=duration, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Course
        fields = '__all__'


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_name', ]


class ContentCreateForm(forms.ModelForm):
    # section = forms.ModelChoiceField(queryset=Section.objects.filter(course=3))
    # text_instruction = forms.FileField(widget=forms.FileInput(attrs={'accept': '.txt', 'class': 'form-control'}))
    # course_video = forms.FileField(widget=forms.FileInput(attrs={'accept': 'video/*', 'class': 'form-control'}))
    # preview_video = forms.FileField(widget=forms.FileInput(attrs={'accept': 'video/*', 'class': 'form-control'}), required=False)
    # resource_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf', 'class': 'form-control'}))

    class Meta:
        model = Content
        fields = '__all__'
        exclude = ['section', ]


class EventCreateForm(forms.ModelForm):
    date_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'time'}))

    class Meta:
        model = models.Events
        fields = '__all__'
