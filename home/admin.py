from django.contrib import admin
from .models import Client, Niveau, Order, OrderItem, Prof, Video, Formation, année, Contact

# Register your models here.
admin.site.register(Client)
admin.site.register(Niveau)
admin.site.register(Prof)
admin.site.register(année)
admin.site.register(Contact)



class ProductImageAdmin(admin.StackedInline):
    model = Video

@admin.register(Formation)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    
 
    class Meta:
       model = Formation


@admin.register(Video)

class ProductImageAdmin(admin.ModelAdmin):
    pass
#-------------------------------------------------

class ProductItemAdmin(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ProductItemAdmin]
 
    class Meta:
       model = Order    

@admin.register(OrderItem)
class ProductItemAdmin(admin.ModelAdmin):
    pass       

#......................................................




    
 






     