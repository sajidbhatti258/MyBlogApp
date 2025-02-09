from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    descripation=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:50px ; height: 50px; border-radius:50% "/>'.format(self.image))
    
    def __str__(self):
        return self.title
        
    
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=200)
    content=models.TextField()
    url=models.CharField( max_length=100)
    cate=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
  
    
    def __str__(self):
        return self.title
    
    
    
    


    
    
    
