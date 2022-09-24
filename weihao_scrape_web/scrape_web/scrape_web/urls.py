"""scrape_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

from app.scrape.views import ScrapeTaskViewSets, ScrapeAccountViewSets, ScrapeResultViewSets
from utils.admin import admin_site

router_backend = routers.DefaultRouter()

router_backend.register('scrape_task', ScrapeTaskViewSets, basename='scrape_task')
router_backend.register('scrape_account', ScrapeAccountViewSets, basename='scrape_account')
router_backend.register('scrape_result', ScrapeResultViewSets, basename='scrape_result')

backend_patterns = [
    path('api/', include(router_backend.urls)),
]


# yasg 自定义设置
class BackendAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/api/'
        return schema


bakcend_schema_view = get_schema_view(openapi.Info(
    title="管理后台接口文档平台",
    default_version='v1',
    description="文档描述",
    terms_of_service="",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
    patterns=backend_patterns,
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=BackendAPISchemeGenerator
)

urlpatterns = [
    path('admin/', admin_site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # swagger配置
    url(r'^api/swagger(?P<format>\.json|\.yaml)$',
        bakcend_schema_view.without_ui(cache_timeout=0),
        name='backend-json'),
    path('api/swagger/', bakcend_schema_view.with_ui('swagger', cache_timeout=0),
         name='backend-swagger'),
    url(r'^api/redoc/$', bakcend_schema_view.with_ui('redoc', cache_timeout=0),
        name='backend-redoc'),
] + backend_patterns
