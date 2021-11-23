from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Blog

# Create your views here.

def BlogHome(request):

    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    # return HttpResponse('This is a Blog Home page')

    return render(request, 'BlogHome.html', context)

def BlogPost(request, slug):

    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    # return HttpResponse('This is a Blog Post page')

    return render(request, 'BlogPost.html', context)