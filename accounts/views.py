from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import get_user_model


User = get_user_model()


def login_view(request):
    form = LoginForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            print(email)
            print(password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index:index'))

            else:
                print('user none')
                print(user)
                return render(request, 'accounts/login.html', {'form': form})
        else:
            print('form invalid')
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index:index'))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index:index'))
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
