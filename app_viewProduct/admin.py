from django.contrib import admin
from app_viewProduct.models import ProductModel

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    model = ProductModel
    list_display = ('excerpt',)

    def excerpt(self, char):
        return self.m_productCaption[:char]

admin.site.register(ProductModel, PostAdmin)