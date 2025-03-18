from django.contrib import admin
from django.template.response import TemplateResponse
from django.db.models import Count
from course.models import Category, Course, Lesson, Comment, Like, Tag
from django.utils.html import mark_safe
from django import forms
from django.urls import path, re_path
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class MyCourseAdminSite(admin.AdminSite):
    site_header = 'eCourseOnline'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
                 ] + super().get_urls()

    def stats_view(self, request):
        course_stats = Category.objects.annotate(course_count=Count('course__id')).values('id', 'name', 'course_count')
        return TemplateResponse(request, 'admin/stats.html', {
            'course_stats': course_stats
        })

admin_site = MyCourseAdminSite(name='iCourse')

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'

class MyCourse(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['name', 'created_date']
    readonly_fields = ['my_image']

    form = CourseForm

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}' />")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }

admin_site.register(Category)
admin_site.register(Course, MyCourse)
admin_site.register(Lesson)
admin_site.register(Comment)
admin_site.register(Like)
admin_site.register(Tag)


