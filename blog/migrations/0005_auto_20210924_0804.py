# Generated by Django 3.1.8 on 2021-09-24 02:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200627_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
