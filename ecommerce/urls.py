"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin

from products.views import UserViewSet, CategoryViewSet, StatViewSet, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('users',
                UserViewSet
                )
router.register('product',
                ProductViewSet
                )

# router.register('category',
#                 CategoryViewSet
#                 )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^category/$',
        CategoryViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='cate-list'
        ),
    url(
        r'^category/(?P<pk>[0-9]+)/$',
        CategoryViewSet.as_view(
            {
                # 'patch':'patial_update',
                'put': 'update',
                'delete':'destroy',
                'get': 'retrieve',
            }
        ),
        name = 'cate-details'
    ),
    url(
        r'^stat/$',
        StatViewSet.as_view(
            {
                'get': 'list',
            }
        )
    ),
    url(
        r'^product/(?P<pk>[0-9]+)/$',
        CategoryViewSet.as_view(
            {
                # 'patch':'patial_update',
                'put': 'update',
                'delete':'destroy',
                'get': 'retrieve',
            }
        ),
        name = 'cate-details'
    ),
    url(r'^', include('products.api_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = urlpatterns + router.urls
