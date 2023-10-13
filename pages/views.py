from django.shortcuts import render, get_object_or_404, redirect
from .models import MainContent, Necklace, Earring, Let, Comment, Comment2, Comment3
from .forms import CommentForm, Comment2Form, Comment3Form
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required



def info(request):
    return render(request, "pages/company_info.html")

def mypage(request):
    return render(request, "pages/mypage.html")

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


@login_required(login_url='accounts:login')
def comment_create(request, product_id):
     product = get_object_or_404(Necklace, pk=product_id)
     if request.method == 'POST':
         form = CommentForm(request.POST)
         if form.is_valid():
             comment = form.save(commit=False)
             comment.content_list = product
             comment.author = request.user
             comment.save()
             return redirect('neckbuy', product_id=product_id)
     else:
        form = CommentForm()
     context = {'product': product, 'form': form}
     return render(request, 'pages/neckbuy.html', context)

@login_required(login_url='accounts:login')
def comment_create2(request, product_id):
    product = get_object_or_404(Earring, pk=product_id)
    if request.method == 'POST':
        form = Comment2Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = product
            comment.author = request.user
            comment.save()
            return redirect('earbuy', product_id=product_id)
    else:
        form = Comment2Form()
    context = {'product': product, 'form': form}
    return render(request, 'pages/earbuy.html', context)

@login_required(login_url='accounts:login')
def comment_create3(request, product_id):
    product = get_object_or_404(Let, pk=product_id)
    if request.method == 'POST':
        form = Comment3Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = product
            comment.author = request.user
            comment.save()
            return redirect('letbuy', product_id=product_id)
    else:
        form = Comment3Form()
    context = {'product': product, 'form': form}
    return render(request, 'pages/letbuy.html', context)


@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
      raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
             comment = form.save(commit=False)
             comment.save()
             return redirect('neckbuy', product_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'pages/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
         raise PermissionDenied
    else:
        comment.delete()
    return redirect('neckbuy', product_id=comment.content_list.id)

@login_required(login_url='accounts:login')
def comment2_update(request, comment_id):
    comment = get_object_or_404(Comment2, id=comment_id)
    if request.user != comment.author:
      raise PermissionDenied
    if request.method == 'POST':
        form = Comment2Form(request.POST, instance=comment)
        if form.is_valid():
             comment = form.save(commit=False)
             comment.save()
             return redirect('earbuy', product_id=comment.content_list.id)
    else:
        form = Comment2Form(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'pages/comment2_form.html', context)

@login_required(login_url='accounts:login')
def comment2_delete(request, comment_id):
    comment = get_object_or_404(Comment2, pk=comment_id)
    if request.user != comment.author:
         raise PermissionDenied
    else:
        comment.delete()
    return redirect('earbuy', product_id=comment.content_list.id)

@login_required(login_url='accounts:login')
def comment3_update(request, comment_id):
    comment = get_object_or_404(Comment3, id=comment_id)
    if request.user != comment.author:
      raise PermissionDenied
    if request.method == 'POST':
        form = Comment3Form(request.POST, instance=comment)
        if form.is_valid():
             comment = form.save(commit=False)
             comment.save()
             return redirect('letbuy', product_id=comment.content_list.id)
    else:
        form = Comment3Form(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'pages/comment3_form.html', context)

@login_required(login_url='accounts:login')
def comment3_delete(request, comment_id):
    comment = get_object_or_404(Comment3, pk=comment_id)
    if request.user != comment.author:
         raise PermissionDenied
    else:
        comment.delete()
    return redirect('letbuy', product_id=comment.content_list.id)


def add_to_cart(request, product_id):

    # 선택한 상품 ID와 옵션(사이즈 및 색상) 가져오기
    size = request.POST.get('size')
    color = request.POST.get('color')

    cart = request.session.get('cart', [])  # 세션에 저장된 장바구니 정보 또는 빈 리스트 가져오기
    cart.append({'product_id': product_id, 'size': size, 'color': color})
    request.session['cart'] = cart  # 세션에 장바구니 정보 저장

    # 장바구니 페이지로 이동
    return redirect('cart')


def cart(request):
    # 장바구니 정보 가져오기
    cart = request.session.get('cart', [])

    return render(request, 'pages/cart.html', {'cart': cart})