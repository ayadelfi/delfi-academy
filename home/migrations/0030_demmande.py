# Generated by Django 3.2.7 on 2021-11-06 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demmande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('wilaya', models.CharField(blank=True, max_length=255, null=True)),
                ('reçu', models.FileField(upload_to='')),
                ('total', models.FloatField(default=0.0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.order')),
            ],
        ),
    ]
