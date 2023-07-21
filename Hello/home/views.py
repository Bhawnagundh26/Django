from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable1":"this is sent",
        "variable2":"this is sent"

    }
    
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'iservices.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.Post.get(name)
        email = request.Post.get(email)
        phone = request.Post.get(phone)
        desc = request.Post.get(desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")


