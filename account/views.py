from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('home')
    return render(request, 'account/dashboard.html')

def products(request):
    # return HttpResponse('products')
    return render(request, 'account/products.html')


def customers(request):
    return render(request, 'account/customers.html')