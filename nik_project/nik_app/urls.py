from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name ="Home"),
    path('product',views.product,name="Product"),
    path('customer/<str:cust_id>',views.customer, name="Customer")
]