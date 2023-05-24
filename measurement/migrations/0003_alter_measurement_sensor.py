# Generated by Django 4.2.1 on 2023-05-24 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]