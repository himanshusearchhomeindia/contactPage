# Generated by Django 3.0.6 on 2021-01-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactPageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontactdata',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]
