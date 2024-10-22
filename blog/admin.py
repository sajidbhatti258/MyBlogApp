from django.contrib import admin
from .models import*

# Register your models here.]


class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','descripation','url','add_date',)
    search_fields=('title',)
    
   
    
    
    
class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cate',)
    
    list_per_page= 50
    
    
    

    class Media:
        js = ('https://cdn.tiny.cloud/1/h33mi5dc2trxqazoz1ug2lojf2jqjz0ykv83o69lmyk2qrdy/tinymce/7/tinymce.min.js','js/script.js',)
    

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
