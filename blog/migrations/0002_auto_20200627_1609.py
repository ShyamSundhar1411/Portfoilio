# Generated by Django 3.0.7 on 2020-06-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dot',
            field=models.DateField(),
        ),
    ]
