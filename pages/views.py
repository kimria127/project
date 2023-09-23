from django.shortcuts import render

def info(request):
    return render(request, "pages/company_info.html")
