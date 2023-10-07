from django.shortcuts import render
from .models import Car
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import CarSerializer
from django.http import JsonResponse


class CarView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def post(self, request):
        car = request.data
        serializer = CarSerializer(car)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cars Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Student")

    def put(self, request, id=None):
        cars_to_update = Car.objects.get(id=id)
        serializer = CarSerializer(
            instance=cars_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cars updated Successfully", safe=False)
        return JsonResponse("Failed To Update Student")
