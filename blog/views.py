from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def blog_page(request):
    blogs = Blog.objects
    return render(request,'blog.html',{'blogs':blogs})


def blog_text(request, blog_id ):
    blog =  get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog_text.html',{'blog':blog})
