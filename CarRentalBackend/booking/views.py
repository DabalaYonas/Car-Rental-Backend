from .models import Booking, Agreement
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import BookingSerializer, AgreementSerializer
from django.http import JsonResponse

class BookingView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def post(self, request):
        data = request.data
        serializer = BookingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Booking Added Successfully", safe=False)
        return JsonResponse("Failed to Add Booking", safe=False)

    def put(self, request, id=None):
        book_to_update = Booking.objects.get(id=id)
        serializer = BookingSerializer(
            instance=book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Booking updated Successfully", safe=False)
        return JsonResponse("Failed To Update Booking")


class AgreementView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = AgreementSerializer
    queryset = Agreement.objects.all()

    def post(self, request):
        data = request.data
        serializer = AgreementSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Agreement Added Successfully", safe=False)
        return JsonResponse("Failed to Add Agreement", safe=False)

    def put(self, request, id=None):
        agreement_to_update = Agreement.objects.get(id=id)
        serializer = AgreementSerializer(
            instance=agreement_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Agreement updated Successfully", safe=False)
        return JsonResponse("Failed To Update Agreement")
