from django.db import models
from Account.models import User
from tinymce.models import HTMLField
import cv2

# Create your models here.
duration = (
    ('one_month', 'One Month'),
    ('two_months', 'Two Months'),
    ('three_months', 'Three Months'),
    ('six_months', 'Six Months'),
    ('one_year', 'One Year'),
)

course_type = (
    ('Business', 'Business'),
    ('Personal', 'Personal'),
)


class CourseCategory(models.Model):
    course_type = models.CharField(max_length=264, choices=course_type)
    category_name = models.CharField(max_length=264)

    def __str__(self):
        return f'{self.course_type} - {self.category_name}'


class Course(models.Model):
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='course_coursecategory')
    course_type = models.CharField(max_length=264, choices=course_type)
    course_name = models.CharField(max_length=264)
    duration = models.CharField(max_length=264, choices=duration)
    price = models.IntegerField()
    short_description = models.TextField(max_length=1000)
    long_description = HTMLField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = 'Courses'


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='section_course')
    section_name = models.CharField(max_length=264)

    def __str__(self):
        return self.section_name


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='content_section')
    lecture_name = models.CharField(max_length=264)
    text_instruction = models.FileField(upload_to='course/')
    course_video = models.FileField(upload_to='course/')
    preview_video = models.FileField(upload_to='course/',
                                     blank=True, null=True)
    resource_file = models.FileField(upload_to='course/')

    def __str__(self):
        return self.lecture_name

    def get_duration(self):
        filename = self.course_video.url

        cap = cv2.VideoCapture(filename[1:])
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        minutes = int(duration / 60)
        seconds = int(duration % 60)

        cap.release()
        return str(minutes) + ':' + str(seconds) + ' m'


class CoursePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coursepurchase_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coursepurchase_course')
    paypal_id = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.full_name} - {self.course.course_name}'


class BCSCourse(models.Model):
    product_id = models.CharField(max_length=255)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE,
                                        related_name='bcscourse_coursecategory')
    # course_type = models.CharField(max_length=264, choices=course_type)
    course_name = models.CharField(max_length=264)
    short_description = models.TextField(max_length=1000)
    long_description = HTMLField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name



class BCSSection(models.Model):
    course = models.ForeignKey(BCSCourse, on_delete=models.CASCADE, related_name='bcssection_bcscourse')
    section_name = models.CharField(max_length=264)

    def __str__(self):
        return self.section_name


class BCSContent(models.Model):
    section = models.ForeignKey(BCSSection, on_delete=models.CASCADE, related_name='bcscontent_bcssection')
    lecture_name = models.CharField(max_length=264)
    text_instruction = models.FileField(upload_to='course/')
    course_video = models.FileField(upload_to='course/')
    preview_video = models.FileField(upload_to='course/',
                                     blank=True, null=True)
    resource_file = models.FileField(upload_to='course/')

    def __str__(self):
        return self.lecture_name

    def get_duration(self):
        filename = self.course_video.url

        cap = cv2.VideoCapture(filename[1:])
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        minutes = int(duration / 60)
        seconds = int(duration % 60)

        cap.release()
        return str(minutes) + ':' + str(seconds) + ' m'
