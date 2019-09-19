from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Create your views here.


def products(request):
    prdct = Product.objects.all()

    paginator = Paginator(prdct, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, template_name='products/index.html', context={'name': request.user, 'products': products,})

def single(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, template_name = 'products/product.html', context = {'product': product})  

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        prdct = Product.objects.filter(title__icontains=q)

        paginator = Paginator(prdct, 18)
        page = request.GET.get('page')
        products = paginator.get_page(page)

        template = 'products/index.html'
        context = { 'query': q, 'products': products}
    else:
        template = 'products/index.html'
        context = {}
      
    return render(request, template, context)

def about(request):
    return render(request=request, template_name="about/about.html")
