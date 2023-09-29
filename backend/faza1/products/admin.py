from django.contrib import admin
from .models import Product, Brand, Category, Cart, Incart, Review, Country, Customer,Complaint
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ('title','rating','brand','category')
admin.site.register(Product,ProductAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display= ('name','id',)
admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name','id',)
admin.site.register(Category,CategoryAdmin)

admin.site.register(Cart)

admin.site.register(Incart)

admin.site.register(Review)

admin.site.register(Country)

admin.site.register(Customer)

admin.site.register(Complaint)