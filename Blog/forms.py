from django import forms
from django.forms import widgets
from Blog import models


class PostForm(forms.ModelForm):
    feature_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    comment_option = forms.ChoiceField(choices=models.COMMENT_OPTIONS, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.Post
        fields = ['post_url', 'title', 'feature_image', 'short_description', 'content',
                  'comment_option', 'tag', ]
