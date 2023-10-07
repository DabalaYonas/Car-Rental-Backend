from .models import Customer
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import CustomerSerializer
from django.http import JsonResponse


class CustomerView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def post(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Customer Added Successfully", safe=False)
        return JsonResponse("Failed to Add Customer", safe=False)

    def put(self, request, id=None):
        customer_to_update = Customer.objects.get(id=id)
        serializer = CustomerSerializer(
            instance=customer_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Customer updated Successfully", safe=False)
        return JsonResponse("Failed To Update Customer")
