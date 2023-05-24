from django.contrib import admin

from .models import Sensor, Measurement


class MeasurementInlineInline(admin.TabularInline):
    model = Measurement


@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    inlines = [MeasurementInlineInline]
    pass


@admin.register(Measurement)
class MeasurementSensor(admin.ModelAdmin):
    pass
