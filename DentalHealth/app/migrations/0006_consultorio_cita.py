# Generated by Django 4.0.6 on 2022-07-26 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('idClinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.clinica')),
                ('idDoctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('hora', models.TimeField(auto_now_add=True, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('estado', models.CharField(max_length=12, null=True)),
                ('idClinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.clinica')),
                ('idConsultorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.consultorio')),
                ('idPaciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.paciente')),
            ],
        ),
    ]
