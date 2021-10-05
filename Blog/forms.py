from django import forms
from Blog import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['post_url', 'title',  'feature_image', 'short_description', 'content',
                  'comment_option', 'tag', ]
