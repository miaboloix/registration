# Generated by Django 3.0.dev20190712152749 on 2019-07-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_course_meeting_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='0', max_length=200),
        ),
    ]