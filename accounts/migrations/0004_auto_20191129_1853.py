# Generated by Django 2.2.5 on 2019-11-29 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191129_1825'),
    ]

    operations = [
        migrations.RenameModel('Person', 'Profile')
    ]
