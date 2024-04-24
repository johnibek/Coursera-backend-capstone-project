from django.contrib import admin
from .models import Booking, Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title__icontains',)

admin.site.register(Booking)
