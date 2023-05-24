from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):

        data = request.data
        print(data['name'], data['description'])
        Sensor(name=data['name'], description=data['description']).save()
        return Response({'status': 'OK'})


class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    #Эта часть написана для RetrieveAPIView, RetrieveUpdateAPIView работает самостоятельно
    # def patch(self, request, pk):
    #     data = request.data
    #     sensor = Sensor.objects.get(id=pk)
    #     sensor.description = data['description']
    #     sensor.save(update_fields=["description"])
    #     return Response({'status': 'OK'})


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = request.data
        print(data['sensor'], data['temperature'])
        Measurement(sensor=Sensor(data['sensor']), temperature=data['temperature']).save()
        return Response({'status': 'OK'})

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
