# Generated by Django 3.1.2 on 2020-10-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0007_auto_20201020_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/LogoColor.JPG', null=True, upload_to='watch/static/profile-pics'),
        ),
    ]
