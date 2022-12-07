from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
