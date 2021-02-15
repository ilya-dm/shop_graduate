"""diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
                  url(r'^order/', include('order.urls', namespace='order')),
                  path('', views.base_view, name='main_page'),
                  path('<str:category_name>/<slug:slug>/', views.object_view, name='object_view'),
                  path('<slug:slug>', views.category_view, name='category_view'),
                  path('login/', views.login_view, name='login'),
                  path('logout/', views.logout_view, name='logout'),
                  path('registration/', views.registration_view, name='registration'),
                  path('cart/', views.cart_view, name='cart'),
                  path(r'add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
                  path(r'delete_item/(?P<product_id>\d+)/$', views.delete_item, name='cart_delete_item'),
                  path(r'delete/(?P<product_id>\d+)/$', views.cart_remove, name='cart_delete_product'),
                  path(r'clear/$', views.cart_clear, name='cart_clear'),
                  path(r'order_failed/$', views.order_failed, name='order_failed'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

