from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path('add/', views.AddAdressAPIView.as_view(), name='add_address'),
    path('paymenet/', views.PaymentAPIView.as_view(), name='paymenet'),
]
