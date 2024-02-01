from django.http import HttpResponse
from django.shortcuts import render



def aboutUs(request):
    return render(request,"aboutus.html")

def product(request):
    return HttpResponse("Welcome to the Product page")

def productDetails(request,productid):
    return HttpResponse(f"view this product {productid}")
def homepage(request):
    data={
        'title':'BabyBedding'
    }
    return render(request,"index.html",data) 


def contact(request):
    return render(request,"contact.html")