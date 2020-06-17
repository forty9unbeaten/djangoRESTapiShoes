from django.conf.urls import include, url
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'shoes', views.ShoeViewSet)
router.register(r'shoe-types', views.ShoeTypeViewset)
router.register(r'shoe-colors', views.ShoeColorViewset)
router.register(r'manufacturers', views.ManufacturerViewset)

url_patterns = [
    url(r'^api/', include(router.urls))
]
