from django.contrib import admin
from .models import Category , Product
# Register your models here.



# pour afficher les elements dans un tableau dans la page du adminstrateur
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',) 
    list_editable = ('price',)


# pour enregister les class creer dans la page admin
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)