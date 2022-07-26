# Generated by Django 4.0.6 on 2022-07-26 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('especialidad', models.CharField(max_length=45)),
                ('cedulaprof', models.CharField(max_length=45)),
                ('idclinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.clinica')),
                ('idcuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cuenta')),
            ],
        ),
    ]