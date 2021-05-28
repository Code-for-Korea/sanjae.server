# Generated by Django 3.2.3 on 2021-05-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("case_app", "0005_auto_20210526_2227"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ruling",
            name="disease",
        ),
        migrations.AddField(
            model_name="ruling",
            name="disease_code",
            field=models.CharField(
                blank=True, default="", help_text="질병코드", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="ruling",
            name="disease_name",
            field=models.CharField(
                blank=True, default="", help_text="질병코드", max_length=255
            ),
        ),
    ]