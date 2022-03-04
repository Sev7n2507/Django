from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Product
from django.utils import timezone
from .forms import ProductForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect


def index(request):

    return render(request, 'app/index.html')


def create_product(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/")

    context['form'] = form
    return render(request, "app/create_product.html", context)


def list_product(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()

    return render(request, "app/list_product.html", context)


def detail_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {}
    if request.method == 'POST':
        substract = request.POST['substract']
        print(substract)
        if int(substract) > product.quantity:
            return HttpResponse('<h1>Vous ne pouvez pas prendre plus de produits que le stock !</h1>')
        else:
            product.quantity = product.quantity - int(substract)
            product.save()

            return HttpResponseRedirect("/app/")

    context["data"] = Product.objects.get(id=id)

    return render(request, "app/detail_product.html", context)


def update_product(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=id)

    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "app/update_product.html", context)


def lobby(request):
    return render(request, "app/lobby.html")
