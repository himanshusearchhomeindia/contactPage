# Generated by Django 3.0.6 on 2021-01-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactPageApp', '0009_usercontactdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontactdata',
            name='phone',
            field=models.CharField(default=None, max_length=12),
        ),
    ]