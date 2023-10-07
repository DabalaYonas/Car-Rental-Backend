from rest_framework import viewsets
from . import serializers, models
from django.http import JsonResponse

class BrandView(viewsets.ModelViewSet):
    serializer_class = serializers.BrandSerializer
    queryset = models.Car_Brand.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.BrandSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Brand Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Brand")

    def put(self, request, id=None):
        model_to_update = models.Car_Brand.objects.get(id=id)
        serializer = serializers.BrandSerializer(
            instance=model_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Brand updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Brand")

class CategoriesView(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Car_Categories.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.CategoriesSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Categories Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Categories")

    def put(self, request, id=None):
        data_to_update = models.Car_Categories.objects.get(id=id)
        serializer = serializers.CategoriesSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Categories updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Categories")


class EngineView(viewsets.ModelViewSet):
    serializer_class = serializers.EngineSerializer
    queryset = models.Car_Engines.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.EngineSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Engine Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Engine")

    def put(self, request, id=None):
        data_to_update = models.Car_Engines.objects.get(id=id)
        serializer = serializers.EngineSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Engine updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Engine")


class TransmissionView(viewsets.ModelViewSet):
    serializer_class = serializers.TransmissionSerializer
    queryset = models.Car_Transmission.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.TransmissionSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Transmission Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Transmission")

    def put(self, request, id=None):
        data_to_update = models.Car_Transmission.objects.get(id=id)
        serializer = serializers.TransmissionSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Transmission updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Transmission")


class ColorView(viewsets.ModelViewSet):
    serializer_class = serializers.ColorSerializer
    queryset = models.Car_Color.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.ColorSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Color Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Color")

    def put(self, request, id=None):
        data_to_update = models.Car_Color.objects.get(id=id)
        serializer = serializers.ColorSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Color updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Color")

class VehicleModelView(viewsets.ModelViewSet):
    serializer_class = serializers.CarModelSerializer
    queryset = models.Car_Model.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.CarModelSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Model Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Car Model")

    def put(self, request, id=None):
        data_to_update = models.Car_Model.objects.get(id=id)
        serializer = serializers.CarModelSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Car Model updated Successfully", safe=False)
        return JsonResponse("Failed To Update Car Model")
