from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone = Phone.objects.all()
    context = {
        'name': phone.name,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug)
    context = {
        'name': phone.name,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
    }
    return render(request, template, context)

