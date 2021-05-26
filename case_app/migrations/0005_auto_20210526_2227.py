# Generated by Django 3.2.3 on 2021-05-26 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case_app', '0004_auto_20210526_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruling',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, help_text='최근 수정 일시'),
        ),
        migrations.AddField(
            model_name='ruling',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, help_text='최근 수정한 사용자', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
