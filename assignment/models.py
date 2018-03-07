import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse
# Create your models here.

def user_validator(value):
    if not re.match('admin', value):
        raise ValidationError('Invalid LngLat Type')

STATUS_CHOICES = (
     ('d', 'Draft'),
     ('p', 'Published'),
     ('w', 'Withdrawn'), )

class Assignment(models.Model):
    #author = models.CharField(max_length=20)
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,help_text='only admin')
    title = models.CharField(max_length=100, verbose_name = 'Title', help_text ='Write the title name within 100 words')
    content = models.TextField(verbose_name ='Content')
    document = models.FileField(blank = True, upload_to='project/documents/%Y/%m')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

#form 작성시 이게 있어야 저장됨
    def get_absolute_url(self):
        return reverse('assignment:assignment_detail', args=[self.id])
