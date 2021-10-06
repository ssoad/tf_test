from django import forms
from django.forms import widgets
from Blog import models


class PostForm(forms.ModelForm):
    # feature_image = forms.
    # comment_option = forms.Select(widget = forms.Select(attr={"class": "form-select"}))
    class Meta:
        model = models.Post
        fields = ['post_url', 'title',  'feature_image', 'short_description', 'content',
                  'comment_option', 'tag', ]
