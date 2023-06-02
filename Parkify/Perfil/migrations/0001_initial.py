# Generated by Django 4.1.2 on 2023-06-01 23:09

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEAFIT',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('cuentaAdmin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdminPARKIFY',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('cuentaAdmin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('organizador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('usuario_ptr', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('password', models.CharField(default='0000', max_length=128)),
                ('username', models.CharField(default='', max_length=128)),
                ('groups', models.ManyToManyField(related_name='usuarios', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='usuarios', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Portero',
            fields=[
                ('usuarioEmpresaVig', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('Perfil.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=50)),
                ('tipoVehiculo', models.CharField(max_length=10)),
                ('combustible', models.CharField(max_length=10)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Perfil.usuario')),
            ],
        ),
    ]
