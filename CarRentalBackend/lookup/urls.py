from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('brands', views.BrandView, 'brands')
router.register('categories', views.CategoriesView, 'categories')
router.register('engines', views.EngineView, 'engines')
router.register('transmissions', views.TransmissionView, 'transmissions')
router.register('colors', views.ColorView, 'colors')
router.register('models', views.VehicleModelView, 'models')

urlpatterns = [
    path('api/', include(router.urls)),
    path('<int:id>/', include(router.urls)),
]
