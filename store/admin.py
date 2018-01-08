from django.contrib import admin
from .models import Customer, Item, Product, invertory
from polls.admin import admin_site
# Register your models here.


class invertoryadmin(admin.ModelAdmin):
    list_display = ('product', 'storeNum', 'soldNum', 'currentStore')


class customeradmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'paymethod', 'referer')


class itemamdin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'expdate',
                    'activedate', 'paprice', 'soldtime')


class productadmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'sprice', 'color')


admin_site.register(Customer, customeradmin)
admin_site.register(Item, itemamdin)
admin_site.register(Product, productadmin)
admin_site.register(invertory, invertoryadmin)
