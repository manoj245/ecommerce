from django.contrib import admin
from .models import Product, Stock,Cart

class Productadmin(admin.ModelAdmin):
    list_display = ['pid','pcat','pname','pdiscnt','pcost','pmfdt','pexpdt','photo']
    list_filter = ['pcat','pmfdt','pexpdt']
    class Meta:
        model=Product
admin.site.register(Product,Productadmin)


class Stockadmin(admin.ModelAdmin):
    list_display = ['pid', 'tot_qty', 'last_update', 'next_update']
    list_filter = ['pid']
    class Meta:
        model = Stock
admin.site.register(Stock,Stockadmin)
class Cartadmin(admin.ModelAdmin):
    list_display = ['username','pid', 'units', 'unitprice', 'tuprice','photo']
    list_filter = ['pid']
    class Meta:
        model = Cart
admin.site.register(Cart,Cartadmin)




