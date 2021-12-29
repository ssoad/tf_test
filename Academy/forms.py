from django import forms
from Academy import models
from Academy.models import duration


class CourseCategoryCreateForm(forms.ModelForm):
    # duration = forms.ChoiceField(choices=duration, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.CourseCategory
        fields = '__all__'
        exclude = ['course_type']


class BCSCourseCreateForm(forms.ModelForm):
    course_category = forms.ModelChoiceField(queryset=models.CourseCategory.objects.filter(course_type='Business'))

    class Meta:
        model = models.BCSCourse
        fields = '__all__'
        exclude = ['product_id']


class PCSCourseCreateForm(forms.ModelForm):
    duration = forms.ChoiceField(choices=duration, widget=forms.Select(attrs={'class': 'form-select'}))
    course_category = forms.ModelChoiceField(queryset=models.CourseCategory.objects.filter(course_type='Personal'))

    class Meta:
        model = models.Course
        fields = '__all__'
        exclude = ['course_type', 'product_id']


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ['section_name', ]


class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = '__all__'
        exclude = ['section', ]

class BCSSectionCreateForm(forms.ModelForm):
    class Meta:
        model = models.BCSSection
        fields = ['section_name', ]


class BCSContentCreateForm(forms.ModelForm):
    class Meta:
        model = models.BCSContent
        fields = '__all__'
        exclude = ['section', ]
