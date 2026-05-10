from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('eye-makeup/', views.eye_makeup, name='eye_makeup'),
    path('eye-makeup/<slug:slug>/', views.eye_makeup_detail, name='eye_makeup_detail'),
    path('fragrance/', views.fragrance, name='fragrance'),
    path('fragrance/<slug:slug>/', views.fragrance_detail, name='fragrance_detail'),
    path('hair-care/', views.hair_care, name='hair_care'),
    path('hair-care/<slug:slug>/', views.hair_care_detail, name='hair_care_detail'),
    path('lipsticks/', views.lipstick, name='lipstick'),
    path('lipsticks/<slug:slug>/', views.lipstick_detail, name='lipstick_detail'),
    path('nails/', views.nail, name='nail'),
    path('nails/<slug:slug>/', views.nail_detail, name='nail_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('offers/', views.offers, name='offers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('track-order/', views.track_order, name='track_order'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('login/', views.login_view, name='login'),
]
