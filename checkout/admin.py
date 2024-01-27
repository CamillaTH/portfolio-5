from django.contrib import admin
from .models import Order, OrderEntry

class OrderEntryAdminInline(admin.TabularInline):
    model = OrderEntry
    readonly_fields = ('entry_total', 'quantity',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderEntryAdminInline,)  # Note the comma to make it a tuple

    readonly_fields = ('order_number', 'date', 'shipping_cost', 'subtotal', 'total_price',)
    
    fields = ('order_number', 'date', 'total_price', 'subtotal', 'full_name', 'first_name', 'last_name', 'email', 'phone', 'postal_code',
              'country', 'city', 'street_address', 'shipping_cost',)

    list_display = ('order_number', 'total_price', 'subtotal', 'date', 'full_name', 'shipping_cost',)  # Added a comma after 'subtotal'

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)