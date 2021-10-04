from django.db import models
from Account.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

# Create your models here.
COMMENT_OPTIONS = (
    ('disabled', 'Disable Comments'),
    ('enabled', 'Enable Comments'),
)
CATEGORY_CHOICES = (
    ('blogs', 'Blog'),
    ('case_studies', 'Case Study'),
    ('podcast', 'Podcast'),
)
SUB_CATEGORY_CHOICES = (
    ('none', 'None'),
    ('business_cybersecurity', 'Business CyberSecurity'),
    ('personal_cybersecurity', 'Personal CyberSecurity'),
    ('hack_recovery', 'Hack Recovery'),
    ('risk_assesment', 'Risk Assesment'),
    ('concierge_cybersecurity', 'Concierge CyberSecurity'),
    ('cybercrime_investigation', 'CyberCrime Investigation'),
)


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    post_url = models.CharField(max_length=264, verbose_name='URL', unique=True)
    title = models.CharField(max_length=264, verbose_name='Add Title')
    category = models.CharField(choices=CATEGORY_CHOICES, default='blogs', max_length=100)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, max_length=100)
    feature_image = models.ImageField(upload_to='blog/', verbose_name='Add Feature Image')
    shot_description = models.TextField(verbose_name='Short Description', max_length=264)
    content = RichTextUploadingField(verbose_name='Post Content')
    reading_time = models.DurationField(default=datetime.timedelta(minutes=3))
    comment_option = models.CharField(choices=COMMENT_OPTIONS, default='disabled', max_length=100)
    tag = models.CharField(max_length=264)
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
