# Generated by Django 5.1.4 on 2024-12-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ImageField(default='', upload_to='images/%Y/%m/%d'),
        ),
    ]
