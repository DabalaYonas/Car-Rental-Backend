
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.BookingView, 'booking')

urlpatterns = [
    path('api/', include(router.urls)),
    path('driver/', include("driver.urls")),
    path('customer/', include("customer.urls")),
    path('payment/', include("payment.urls")),
]
