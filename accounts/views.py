from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


def join(request):
    errors={}
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors
    else:
        form = SignupForm()
    return render(request, 'accounts/join.html', {'form': form, 'errors': errors})

def mypage(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        # 닉네임 대신 아이디(Username)를 표시
        return render(request, 'accounts/mypage.html', {'username': request.user.username})
    else:
        return redirect('login')