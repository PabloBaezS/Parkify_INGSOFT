# Generated by Django 4.1.2 on 2023-06-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacionCelda', models.CharField(max_length=50)),
                ('tipoVehiculo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('idError', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('infoError', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parqueadero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField(default=0)),
                ('errores', models.ManyToManyField(to='Parqueadero.error')),
            ],
        ),
    ]
