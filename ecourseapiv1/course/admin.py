from django.contrib import admin
from course.models import Category, Course, Lesson, Comment, Like, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

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

admin.site.register(Category)
admin.site.register(Course, MyCourse)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)


