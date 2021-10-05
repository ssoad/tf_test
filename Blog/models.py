from django.db import models
from Account.models import User

from tinymce.models import HTMLField
import datetime

# Create your models here.
COMMENT_OPTIONS = (
    ('disabled', 'Disable Comments'),
    ('enabled', 'Enable Comments'),
)



class BlogCategory(models.Model):
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Blog Categories'


class BlogSubCategory(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='subcategory_category')
    sub_category = models.CharField(max_length=80)

    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name_plural = 'Blog Sub Categories'


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    post_url = models.CharField(max_length=264, verbose_name='URL', unique=True)
    title = models.CharField(max_length=264, verbose_name='Add Title')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='post_category')
    sub_categories = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE, related_name='post_sub_category')
    feature_image = models.ImageField(upload_to='blog/', verbose_name='Add Feature Image')
    short_description = models.TextField(verbose_name='Short Description', max_length=264)
    content = HTMLField(verbose_name='Post Content')
    # reading_time = models.DurationField(default=datetime.timedelta(minutes=3))
    comment_option = models.CharField(choices=COMMENT_OPTIONS, default='disabled', max_length=100)
    tag = models.CharField(max_length=264)
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comment = models.TextField(verbose_name='Comment', max_length=500)

    def __str__(self):
        return f'{self.post.title}\'s comment'
