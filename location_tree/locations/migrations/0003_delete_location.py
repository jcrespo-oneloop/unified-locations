# Generated by Django 2.2.2 on 2019-06-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]