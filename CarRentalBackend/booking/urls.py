
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.BookingView, 'booking')

router2 = routers.DefaultRouter()
router2.register('api', views.AgreementView, 'agreement')

urlpatterns = [
    path('api/', include(router.urls)),
    path('agreement/', include(router2.urls)),
    path('driver/', include("driver.urls")),
    path('customer/', include("customer.urls")),
    path('payment/', include("payment.urls")),
]
