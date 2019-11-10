from django.contrib import admin

# Register your models here.
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']  # 后台显示产品模块


admin.site.register(Product, ProductAdmin)
