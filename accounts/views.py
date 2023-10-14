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

