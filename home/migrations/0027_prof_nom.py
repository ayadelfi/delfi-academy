# Generated by Django 3.2.7 on 2021-10-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_formation_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
