# Generated by Django 3.0.6 on 2021-01-27 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactPageApp', '0007_remove_usercontactdata_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserContactData',
        ),
    ]