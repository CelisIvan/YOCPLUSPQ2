# Generated by Django 2.2.5 on 2019-12-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20191201_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='codigo',
            field=models.DateTimeField(),
        ),
    ]
