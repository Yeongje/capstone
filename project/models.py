import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

STATUS_CHOICES = (
     ('d', 'Draft'),
     ('p', 'Published'),
     ('w', 'Withdrawn'), )

INDUSTRY_CHOICES = (
     ('Web Application', 'Web Application'),
     ('Mobile Application', 'Mobile Application'),
     ('Software', 'Software'),
     ('Hardware', 'Hardware'),
     ('Data', 'Data'), )

class Post(models.Model):
    #author = models.CharField(max_length=20)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name = 'Title', help_text ='Write the title name within 100 words')
    content = models.TextField(verbose_name ='Content')
    document = models.FileField(blank = True, upload_to='project/documents/%Y/%m')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    category = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.title

#form 작성시 이게 있어야 저장됨
    def get_absolute_url(self):
        return reverse('project:post_detail', args=[self.id])

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.PROTECT)
    author = models.CharField(max_length=20)
    message = models.TextField()
    document = models.FileField(blank = True, upload_to='project/documents/%Y/%m')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
