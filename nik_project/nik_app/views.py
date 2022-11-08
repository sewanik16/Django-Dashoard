from django.shortcuts import render
from .models import Product, Customer, Order

# Create your views here.
def dashboard(request):
    person = Customer.objects.all()
    order = Order.objects.all()
    total_orders = order.count()
    orders_deliverd = order.filter(status = 'Delivered').count()
    orders_pending = order.filter(status = 'Pending').count()
    out_for_delivery = total_orders - (orders_deliverd + orders_pending)
    context = {
        'person': person,
        'order': order,
        'total_orders':total_orders,
        'orders_deliverd':orders_deliverd,
        'orders_pending':orders_pending,
        'out_for_delivery':out_for_delivery
    }
    return render(request,'nik-app/dashboard.html', context)

def product(request):
    item = Product.objects.all()
    totalItem = item.count()
    context = {
        'item': item,
        'totalItem': totalItem
    }
    return render(request,'nik-app/product.html', context)

def customer(request,cust_id):
    customer = Customer.objects.all()
    user = customer.filter(id=cust_id)
    orders = Order.objects.all()
    order = orders.filter(customer = cust_id)
    totalOrder = order.count()
    return render(request,'nik-app/customer.html',{'user':user[0],'customer':user,'order':order,'totalOrder':totalOrder})
