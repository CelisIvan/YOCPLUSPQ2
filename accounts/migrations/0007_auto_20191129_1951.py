# Generated by Django 2.2.5 on 2019-11-29 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191129_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Estado'),
        ),
    ]