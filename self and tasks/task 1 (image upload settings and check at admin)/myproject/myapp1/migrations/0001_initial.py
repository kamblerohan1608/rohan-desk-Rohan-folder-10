# Generated by Django 4.1 on 2022-09-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myappModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100)),
                ('image_description', models.CharField(max_length=100)),
                ('image_photo', models.ImageField(upload_to='profile_image/')),
            ],
        ),
    ]
