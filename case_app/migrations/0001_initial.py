# Generated by Django 3.2.3 on 2021-05-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(help_text='사건번호', max_length=255)),
                ('court_name', models.CharField(help_text='법원', max_length=255)),
                ('ruling_type', models.CharField(blank=True, help_text='판결유형', max_length=255)),
                ('case_type', models.CharField(blank=True, help_text='사건유형', max_length=255)),
                ('issue_category', models.CharField(blank=True, help_text='사고질병구분', max_length=255)),
                ('ruling_text', models.TextField(help_text='판결문')),
                ('case_title', models.CharField(help_text='제목', max_length=255)),
                ('related_case', models.CharField(blank=True, help_text='연관사건', max_length=255)),
                ('working_condition', models.TextField(blank=True, help_text='업무환경')),
                ('disease_code', models.CharField(blank=True, default='', help_text='질병코드', max_length=255)),
                ('disease_name', models.CharField(blank=True, default='', help_text='질병명', max_length=255)),
            ],
        ),
    ]
