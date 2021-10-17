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


class Course(models.Model):
    course_name = models.CharField(max_length=264)
    duration = models.CharField(max_length=264, choices=duration)
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
        print(filename)

        cap = cv2.VideoCapture(filename[1:])
        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        minutes = int(duration / 60)
        seconds = int(duration % 60)

        cap.release()
        return str(minutes) + ':' + str(seconds) + ' m'
