from django.shortcuts import render,redirect
from .forms import VendorForm
from .models import Vendor

# Create your views here.
def inventory_base(request):
    # This view function displays the base page with a welcome message.
    return render(request, 'inventory/base.html') 

def supply_page(request):
    return render(request, 'inventory/supply_page.html')

def vendors_page(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/vendors_page.html', {'vendors': vendors})


def register_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supply_page')
    else:
        form = VendorForm()
    return render(request, 'inventory/register_vendor.html', {'form': form})


def order_logs_page(request):
    return render(request, 'inventory/order_logs_page.html')

def order_history(request):
    return render(request, 'inventory/order_history.html')

