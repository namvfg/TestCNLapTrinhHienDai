# Generated by Django 5.1.6 on 2025-02-28 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_tag_lesson_comment_course_tags_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
    ]
