from django import forms
from BusinessSecurity import models


class AddServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        fields = '__all__'


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'has_sub_service', 'is_subscription_based', 'service_header', 'service_body', 'service_footer',]

