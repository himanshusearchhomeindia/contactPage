# Generated by Django 3.0.6 on 2021-01-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactPageApp', '0002_auto_20210127_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontactdata',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
