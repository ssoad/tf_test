from django import forms
from Blog import models
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ['post_url', 'title', 'category', 'sub_categories', 'feature_image', 'short_description', 'content',
                  'comment_option', 'tag', ]
