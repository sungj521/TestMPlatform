# Generated by Django 2.0 on 2020-01-04 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_serviceinfo_status'),
        ('api', '0002_testenv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestEnv',
            new_name='RunEnv',
        ),
    ]
