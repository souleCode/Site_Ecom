from django.contrib import admin
from .models import Category, Product,Commande

# Register your models here.

#----------------------
admin.site.site_header ='E-Commerce'
admin.site.site_title = "Aliza-Shope"
admin.site.index_title =" Manageur"



#-----------------------------------
class AdminCategory(admin.ModelAdmin):
    list_display =('name','date_added')
    
class AdminProduct(admin.ModelAdmin):
    list_display =('title','category','date_added','price')   
    search_fields = ('title',)
    list_editable =('price',)

class AdminCommande(admin.ModelAdmin):
    list_display =('items','nom','email','address','date_commande','ville','pays','total')    
    


admin.site.register(Category,AdminCategory )
admin.site.register(Product,AdminProduct) 
admin.site.register(Commande,AdminCommande)   