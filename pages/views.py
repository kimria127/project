from django.shortcuts import render
from .models import MainContent
def info(request):
    return render(request, "pages/company_info.html")

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'pages/content_list.html',context)

def login(request):
    return render(request, "pages/login.html")
