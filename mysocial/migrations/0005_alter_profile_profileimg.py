# Generated by Django 4.1 on 2023-06-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysocial', '0004_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_images'),
        ),
    ]
