# Generated by Django 4.1.7 on 2023-03-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioucn', '0002_alter_reserva_idreserva'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='equipos',
            name='IdEquipo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='soportes',
            name='IdSoporte',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
