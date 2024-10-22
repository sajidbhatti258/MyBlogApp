from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category

# Create your views here.

def home(request):
    #load all the post from db
    post=Post.objects.all()[:11]
    # print(posts)
    cat=Category.objects.all()
    
    data={
            'post':post,
            'cat':cat,
    }
    
    
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    cat=Category.objects.all()
    
    
    return render(request,'post.html',{'post':post,'cat':cat})


def category(request,url):
    
    cate=Category.objects.get(url=url)
    post=Post.objects.filter(cate=cate)
    
    return render(request,"category.html",{'cate':cate,'post':post})
    
    
    
