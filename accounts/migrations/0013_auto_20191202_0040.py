# Generated by Django 2.2.5 on 2019-12-02 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191202_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boleto',
            old_name='user_id',
            new_name='user',
        ),
    ]
