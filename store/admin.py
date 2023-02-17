from django.contrib import admin
from store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_cat','quantity','price','descriptions')
admin.site.register(Product,ProductAdmin)