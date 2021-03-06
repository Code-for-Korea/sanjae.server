# Generated by Django 3.2.3 on 2021-05-26 12:52
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("case_app", "0003_auto_20210526_2148"),
    ]

    operations = [
        migrations.AddField(
            model_name="ruling",
            name="causality",
            field=models.TextField(blank=True, help_text="상당인과관계"),
        ),
        migrations.AlterField(
            model_name="ruling",
            name="disease",
            field=models.CharField(blank=True,
                                   default="",
                                   help_text="질병분류",
                                   max_length=255),
        ),
    ]
