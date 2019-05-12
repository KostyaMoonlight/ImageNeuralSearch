from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, ProductForm
from .managers import DBManager
import os
 
def handle_uploaded_file(name, file):
    name = f'IMAGES/{name}'
    #os.mkdir('IMAGES')
    with open(name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def index(request):
    db = DBManager()
    if request.method == "POST":
        name = request.POST.get("info")
        image = request.POST.get("image")
        handle_uploaded_file(str(request.FILES['image']), request.FILES['image'])
        success = 'true'        
        return HttpResponse("<h2>Hello, {0}</h2><h2>{1}</h2><h2>{2}</h2>".format(name, request.FILES['image'], success))
    else:
        data = {'form' : UserForm()}    
        return render(request, "home.html", context=data)

    
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def upload_product(request):
    db = DBManager()
    if request.method == "POST":
        name = request.POST.get("info")
        url = request.POST.get("url")
        image = request.POST.get("image")
        handle_uploaded_file(str(request.FILES['image']), request.FILES['image'])     
        return HttpResponse("<h2>Product: {0}</h2><h2>{1}</h2><h2>{2}</h2>".format(name, request.FILES['image'], url))
    else:
        data = {'form' : ProductForm()}    
        return render(request, "home/upload_product.html", context=data)

def view_history(request):
    return HttpResponse("<h2>Контакты</h2>")

def view_all_history(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)
 
def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)