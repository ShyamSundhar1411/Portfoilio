# Generated by Django 3.0.7 on 2020-06-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='', verbose_name='images/')),
                ('descriptionn', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
