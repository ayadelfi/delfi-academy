# Generated by Django 3.2.7 on 2021-11-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_demmande_reçu'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='reçu',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='wilaya',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]