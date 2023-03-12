# Generated by Django 4.1.7 on 2023-03-09 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('IdEquipo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=30)),
                ('Modelo', models.CharField(max_length=30)),
                ('Marca', models.CharField(max_length=30)),
                ('IdUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Soportes',
            fields=[
                ('IdSoporte', models.BigIntegerField(primary_key=True, serialize=False)),
                ('TipoSoporte', models.IntegerField()),
                ('FechaInicio', models.DateTimeField()),
                ('FechaFinal', models.DateTimeField(null=True)),
                ('IdEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioucn.equipos')),
                ('IdUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('IdReserva', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Detalle', models.CharField(max_length=100, null=True)),
                ('FechaInicio', models.DateTimeField()),
                ('FechaFinal', models.DateTimeField(null=True)),
                ('IdEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioucn.equipos')),
                ('IdUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
