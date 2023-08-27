
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.BookingView, 'booking')

router2 = routers.DefaultRouter()
router2.register('', views.DriverView, 'driver')

urlpatterns = [
    path('api/', include(router.urls)),
    path('driver/api/', include(router2.urls)),
    path('payment/', include("payment.urls")),
]
