from django import forms
from Academy import models
from Academy.models import duration


class CourseCreateForm(forms.ModelForm):
    duration = forms.ChoiceField(choices=duration, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.Course
        fields = '__all__'
        exclude = ['course_type']


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ['section_name', ]


class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = '__all__'
        exclude = ['section', ]
