"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from . import views

router = routers.DefaultRouter()


# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.test),
    url(r'^set_params/$', views.set_params),

    url(r'^diagram/(?P<pk>\S+)$', views.diagrapm),
    url(r'^3d/(?P<pk>\S+)$', views.diagrapm_3D),
    url(r'^nodes', views.nodes),
    url(r'^fix_nodes', views.nodes_fix),
    url(r'^echart/$', views.echart_test),
    url(r'^socket/$', views.socket_test),
    url(r'^humiditys/$', views.humidity_list),
    url(r'^temperatures/$', views.temperature_list),
    url(r'^end_devices/$', views.end_device_list),
    url(r'^humiditys/(?P<pk>\S+)/$', views.humidity_detail),
    url(r'^temperatures/(?P<pk>\S+)/$', views.temperature_detail),
    url(r'^end_devices/(?P<pk>\S+)/$', views.end_device_detail),
    url(r'^humiditys1/$', views.HumidityList.as_view()),
    url(r'^net_param/$', views.NetParamList.as_view()),
    url(r'^humiditys1/(?P<pk>\S+)/$', views.HumidityDetial.as_view()),
    url(r'^temperatures1/$', views.TemperatureList.as_view()),
    url(r'^temperatures1/(?P<pk>\S+)/$', views.TemperatureDetial.as_view()),
    url(r'^end_devices1/$', views.EndDeviceList.as_view()),
    url(r'^end_devices1/(?P<pk>\S+)/$', views.EndDeviceDetial.as_view()),
    url(r'^end_devices_info/$', views.EndDeviceInfoList.as_view()),
    url(r'^enddevice_tooltip/(?P<pk>\S+)$', views.end_device_tooltip),
]
