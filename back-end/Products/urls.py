from django.urls import path
from . import views

app_name = "Prodcuts"


urlpatterns = [
    path('', views.ListProductsAPIView.as_view(), name="products"),
    path('categories/', views.CatsListAPIView.as_view(), name="categories"),
    path('cart/', views.CartAPIView.as_view(), name="cart"),
    path('<str:pk>/', views.SingleProductAPIView.as_view(), name="product"),
    path('category/<str:pk>/',
         views.CategoryProductsAPIView.as_view(), name="category"),
    path('add-to-cart/<str:pk>/', views.AddToCartAPIView.as_view(), name='addToCart'),
    path('decrease-qt/<str:pk>/',
         views.DecreaseQtAPIView.as_view(), name='decreaseQt'),
    path('Remove-from-cart/<str:pk>/',
         views.RemoveFromCartAPIView.as_view(), name='RemoveFromCart'),
]
