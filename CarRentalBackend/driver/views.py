from .models import Driver
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import DriverSerializer
from django.http import JsonResponse


class DriverView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def post(self, request):
        data = request.data
        serializer = DriverSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Driver Added Successfully", safe=False)
        return JsonResponse("Failed to Add Driver", safe=False)

    def put(self, request, id=None):
        driver_to_update = Driver.objects.get(id=id)
        serializer = DriverSerializer(
            instance=driver_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Driver updated Successfully", safe=False)
        return JsonResponse("Failed To Update Driver")
