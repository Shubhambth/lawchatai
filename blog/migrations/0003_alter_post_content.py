# Generated by Django 5.1.7 on 2025-03-20 05:29

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
