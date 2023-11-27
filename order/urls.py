"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'order'  # Namespace for the app


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.category_products, name='category_products'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.searchmenu, name='search'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('removeitems/<int:product_id>/', views.removeitems, name='removeitems'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('resetter/', views.resetter, name='resetter'),
    path('productsdetails/<int:product_id>/', views.productdetails, name='productdetails'),
    path('update_data', views.update_data, name='update_data'),
    path('delete_data', views.delete_data, name='delete_data'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
