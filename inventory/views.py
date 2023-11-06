import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import VendorForm, ItemForm
from .models import Vendor, Item, Quantity, Logs

# Create your views here.
def save_logs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Access the data
            vendor = data.get('vendor')
            date = data.get('date')
            table_data = data.get('tableData')

            # Iterate through the list of key-value pairs
            items = []
            for row in table_data:
                item_id = row.get('item')
                quantity = row.get('quantity')
                if item_id and quantity:
                    # Query the Item model to get the name based on the item_id
                    item = Item.objects.get(id=item_id)
                    items.append({"item_name": item.name, "quantity": quantity})
                    new_qty = item.qty + int(quantity) #update item quantity
                    item.qty = new_qty
                    item.save()

            # Create a Logs object with the collected data
            logs = Logs(vendor=vendor, items=json.dumps(items), date=date)

            # Save the object to the database
            logs.save()

            # Redirect to the same page with a success message in the URL query string
            return redirect('/inventory/order-log/log-order', success_message='Order logged')

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    # If not a POST request, render the page
    success_message = request.GET.get('success_message', None)
    return render(request, 'inventory/log_order.html', {'vendors': vendor, 'items': items, 'success_message': success_message})



def log_order(request):
    items = Item.objects.all()
    quantities = Quantity.objects.all()
    vendors = Vendor.objects.all()

    return render(request, 'inventory/log_order.html', {'items': items, 'quantities': quantities,'vendors': vendors})

def inventory_base(request):
    # This view function displays the base page with a welcome message.
    return render(request, 'inventory/base.html') 

def supply_page(request):
    return render(request, 'inventory/supply_page.html')

def orders_page(request):
    return render(request, 'inventory/orders_page.html')

def pending_orders(request):
    return render(request, 'inventory/pending_orders.html')

def completed_orders(request):
    return render(request, 'inventory/completed_orders.html')

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
            return redirect('supply_page')
    else:
        form = VendorForm()
    return render(request, 'inventory/register_vendor.html', {'form': form})

def register_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supply_page')
    else:
        form = ItemForm()
    return render(request, 'inventory/register_item.html', {'form': form})


def order_logs_page(request):
    return render(request, 'inventory/order_logs_page.html')

def order_history(request):
    logs = Logs.objects.all()
    return render(request, 'inventory/order_history.html',{'logs':logs})

