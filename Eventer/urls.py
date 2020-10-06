"""Eventer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import products, single, search, about
from carts.views import view, add_to_cart, remove_from_cart
from registration.views import register, logout_request, login_request
from orders.views import checkout, orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products, name='home'),
    path('pr/<slug>/', single, name='single'),
    path('s/', search, name='search'),
    path('cart/', view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='user_orders'),
    path('cart/<id>\d+/', remove_from_cart, name='remove_from_cart'),
    path('cart/<slug>[\w-]+/', add_to_cart, name='add_to_cart'),
    path("register/", register, name="register"),
    path("logout/", logout_request, name="logout"),
    path("login/", login_request, name="login"),
    path("about/", about, name="about"),
    #path("partners/", partners, name="partners"),
    #path("create_event/", create_event, name="create_event"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
