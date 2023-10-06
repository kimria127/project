from django.shortcuts import render, get_object_or_404
from .models import MainContent, Necklace, Earring, Let
def info(request):
    return render(request, "pages/company_info.html")

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'pages/content.html',context)

def contentN(request):
    necklaces = Necklace.objects.all()
    return render(request, "pages/content_necklace.html", {"necklaces": necklaces})
def neckbuy(request, product_id):
    product = get_object_or_404(Necklace, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'pages/neckbuy.html', context)
def contentE(request):
    earrings = Earring.objects.all()
    return render(request, "pages/content_earring.html",  {"earrings": earrings})
def earbuy(request, product_id):
    product = get_object_or_404(Earring, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'pages/earbuy.html', context)
def contentL(request):
    lets = Let.objects.all()
    return render(request, "pages/content_let.html",  {"lets": lets})

def letbuy(request, product_id):
    product = get_object_or_404(Let, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'pages/letbuy.html', context)

def detail(request, content_id):
    content_list=MainContent.objects.get(id=content_id)
    context={'content_list':content_list}
    return render(request, "pages/n-detail.html",context)




