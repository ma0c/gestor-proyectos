# Generated by Django 2.1.2 on 2018-11-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField()),
                ('numero_usuarios', models.CharField(max_length=80)),
                ('duracion', models.CharField(max_length=80)),
                ('ubicacion', models.CharField(max_length=80)),
                ('categoria', models.CharField(max_length=80)),
            ],
        ),
    ]
