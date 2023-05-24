from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название датчика')
    description = models.CharField(max_length=50, verbose_name='Описание датчика')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    def __str__(self):
        return self.sensor.name
