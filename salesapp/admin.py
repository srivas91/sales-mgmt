from django.contrib import admin

# Register your models here.
from salesapp.models import SaleDetail, Item

class ItemAdmin(admin.ModelAdmin):
    list_display =['name','default_price']

class SaleAdmin(admin.ModelAdmin):
    list_display = ['item','quantity','unit_price']

admin.site.register(Item,ItemAdmin)
admin.site.register(SaleDetail,SaleAdmin)