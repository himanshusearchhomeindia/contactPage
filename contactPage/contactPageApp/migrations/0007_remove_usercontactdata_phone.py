# Generated by Django 3.0.6 on 2021-01-27 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactPageApp', '0006_auto_20210127_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontactdata',
            name='phone',
        ),
    ]