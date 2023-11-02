from django.contrib import admin
from .models import Vendor, Item, Quantity, Logs

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Logs)

@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity')
