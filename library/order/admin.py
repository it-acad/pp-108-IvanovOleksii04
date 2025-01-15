from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'get_status')
    search_fields = ('book__name', 'user__username')
    list_filter = ('created_at', 'book')  # Видалено 'user__username', якщо його немає
    ordering = ('-created_at',)

    fieldsets = (
        ('Order Information', {
            'fields': ('book', 'user', 'created_at', 'end_at')
        }),
    )

    def get_status(self, obj):
        """Display the status of an order."""
        return 'Closed' if obj.end_at else 'Pending'
    get_status.admin_order_field = 'end_at'
    get_status.short_description = 'Status'
