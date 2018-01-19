from django.contrib import admin
from .models import Assignment
from django.utils.safestring import mark_safe
# Register your models here.

# admin.site.register(Post)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','status','created_at','updated_at']

    actions =['make_published']

    def content_size(self,assignment):
        return mark_safe('<strong>{}</strong>Words'.format(len(assignment.content)))
    content_size.short_description = 'the number of words '


    def make_published(self,request,queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description ='change the status of assignment to published'
