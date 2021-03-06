# Generated by Django 2.2.5 on 2019-11-26 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.FloatField()),
                ('descripcion', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('asistentes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('edad', models.IntegerField()),
                ('empresa', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='info', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Evento')),
            ],
        ),
    ]
