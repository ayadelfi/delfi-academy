# Generated by Django 3.2.7 on 2021-12-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_alter_formation_série'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duré_video',
            field=models.CharField(default='', max_length=255),
        ),
    ]
