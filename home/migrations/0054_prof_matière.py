# Generated by Django 3.2.7 on 2021-12-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_video_duré_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='matière',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
