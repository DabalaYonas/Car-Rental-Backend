from .models import Payment
from rest_framework import viewsets
from .serializers import PaymentSerializer


class PaymentView(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Payment Added Successfully", safe=False)
        return JsonResponse("Failed to Add Payment", safe=False)

    def put(self, request, id=None):
        payment_to_update = Payment.objects.get(id=id)
        serializer = PaymentSerializer(
            instance=payment_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Payment updated Successfully", safe=False)
        return JsonResponse("Failed To Update Payment")
