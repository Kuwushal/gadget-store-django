from django.contrib import admin
from . models import Product


class ProductAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'price', 'is_featured', 'image', 'description')

    
    search_fields = ('name', 'description', 'price')

 
    list_filter = ('is_featured',)


    list_editable = ('is_featured',)

 
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image', 'is_featured')
        }),
    )


    list_per_page = 20

admin.site.register(Product)