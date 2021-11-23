from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Contact
from Blog.models import Blog

# Create your views here.

# --------------------------------------------------------

# Admin Panel~
# Username = Udoy
# email = srudoy436@gmai.com
# password = udoy436

# --------------------------------------------------------


def home(request):
    # return HttpResponse('This is a Home Page')

    return render(request, 'home.html')


def about(request):
    # return HttpResponse('This is a About page')

    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        textarea = request.POST.get('textarea')

        if  username == '':
            messages.error(request, 'Oops! Please Type Your Username - Try Again')

        elif not username.islower():
            messages.error(request, 'Oops! Please Type a Small Latter Username - Try Again')

        elif phone == '':
            messages.error(request, 'Oops! Please Type Your Phone Number - Try Again')

        elif not phone.isdecimal():
            messages.error(request, 'Oops! Your Phone Number is Not Correct - Try Again')

        elif email == '':
            messages.error(request, 'Oops! Please Type Your Email Address - Try Again')

        elif address == '':
            messages.error(request, 'Oops! Please Type Your Address - Try Again')

        else:
            context = Contact(username=username, name=name, phone=phone, email=email, address=address, textarea=textarea)
            context.save()
            messages.success(request, 'Thank You For Contact Us')


        # print(username, name, phone, email, address, textarea) 

    # return HttpResponse('This is a Contact page')

    return render(request, 'contact.html')


def search(request):
    query = request.GET['query']

    if len(query) > 80:
        allPost = Blog.objects.none()
    else:
        allPostTitle = Blog.objects.filter(title__icontains=query)
        allPostContent = Blog.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)

        params = {'allPost':allPost, 'query':query}

    return render(request, 'search.html', params)