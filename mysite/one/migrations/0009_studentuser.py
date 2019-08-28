# Generated by Django 3.0.dev20190712152749 on 2019-07-26 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('one', '0008_auto_20190725_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hopid', models.CharField(max_length=200)),
                ('jhed', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=100)),
                ('grad_year', models.CharField(max_length=4)),
                ('pre_health', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]