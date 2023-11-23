import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.views.decorators.http import require_POST
from .forms import VendorForm, ItemForm
from .models import Vendor, Item, Quantity, Logs, Orders
from datetime import date

def save_logs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            vendor = data.get('vendor')
            date = data.get('date')
            table_data = data.get('tableData')
            items = []
            for row in table_data:
                item_id = row.get('item')
                quantity = row.get('quantity')
                if item_id and quantity:
                    item = Item.objects.get(id=item_id)
                    items.append({"item_name": item.name, "quantity": quantity})
                    new_qty = item.qty + int(quantity)
                    item.qty = new_qty
                    item.save()
            logs = Logs(vendor=vendor, items=json.dumps(items), date=date)
            logs.save()
            return redirect('/inventory/order-log/log-order', success_message='Order logged')
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    success_message = request.GET.get('success_message', None)
    return render(request, 'inventory/log_order.html', {'vendors': vendor, 'items': items, 'success_message': success_message})

def log_pending(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            franchise = data.get('user')
            table_data = data.get('tableData')
            items = []
            for row in table_data:
                item_id = row.get('item')
                quantity = row.get('quantity')
                if item_id and quantity:
                    item = Item.objects.get(id=item_id)
                    items.append({"item_name": item.name, "quantity": quantity})
            orders = Orders(franchise=franchise, items=json.dumps(items))
            orders.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    success_message = request.GET.get('success_message', None)
    return render(request, 'inventory/log_order.html', {'items': items, 'success_message': success_message})

def log_order(request):
    items = Item.objects.all()
    quantities = Quantity.objects.all()
    vendors = Vendor.objects.all()
    return render(request, 'inventory/log_order.html', {'items': items, 'quantities': quantities,'vendors': vendors})

def inventory_base(request):
    items = Item.objects.all()
    return render(request, 'inventory/base.html',{'items': items}) 

def supply_page(request):
    logs = Logs.objects.all()
    return render(request, 'inventory/supply_page.html',{'logs': logs} )

def orders_page(request):
    orders = Orders.objects.filter(completed=False)
    return render(request, 'inventory/orders_page.html',{'orders':orders})

def pending_orders(request):
    orders = Orders.objects.filter(completed=False)
    return render(request, 'inventory/pending_orders.html', {'orders':orders})

def completed_orders(request):
    orders = Orders.objects.filter(completed=True)
    return render(request, 'inventory/completed_orders.html',{'orders':orders})

def vendors_page(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/vendors_page.html', {'vendors': vendors})

def items_page(request):
    items = Item.objects.all()
    return render(request, 'inventory/items_page.html', {'items': items})

def register_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendors_page')
    else:
        form = VendorForm()
    return render(request, 'inventory/register_vendor.html', {'form': form})

def register_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items_page')
    else:
        form = ItemForm()
    return render(request, 'inventory/register_item.html', {'form': form})

def order_logs_page(request):
    return render(request, 'inventory/order_logs_page.html')

def order_history(request):
    logs = Logs.objects.all()
    return render(request, 'inventory/order_history.html',{'logs':logs})

@require_POST
def update_orders(request):
    data = json.loads(request.body)
    order_ids = data.get('orderIds', [])
    Orders.objects.filter(id__in=order_ids).update(completed=True, delivery_date=date.today())
    for order_id in order_ids:
        order = Orders.objects.get(id=order_id)
        order_items = json.loads(order.items)
        for order_item in order_items:
            item_name = order_item['item_name']
            quantity = int(order_item['quantity'])
            item = Item.objects.get(name=item_name)
            new_qty = item.qty - quantity
            item.qty = new_qty
            item.save()
    return JsonResponse({'message': 'Orders and items updated successfully'})

def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendors_page')
    return render(request, 'inventory/delete_vendor.html', {'vendor': vendor})

def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendors_page')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'inventory/edit_vendor.html', {'form': form, 'vendor': vendor})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('items_page')
    return render(request, 'inventory/delete_item.html', {'item': item})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items_page')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form, 'item': item})
