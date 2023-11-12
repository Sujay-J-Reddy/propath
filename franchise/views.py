from django.shortcuts import render
from inventory.models import Item, Orders

# Create your views here.
def base_page(request):
    return render(request, 'franchise/base.html')

def new_order(request):
    items = Item.objects.all()
    return render(request, 'franchise/new_order.html',{'items':items})

def orders(request):
    return render(request, 'franchise/orders.html')

def orders_completed(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=True,franchise=user_franchise)

    return render(request, 'franchise/orders_completed.html',{'orders':orders})


def orders_pending(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=False,franchise=user_franchise)

    return render(request, 'franchise/orders_pending.html',{'orders':orders})
