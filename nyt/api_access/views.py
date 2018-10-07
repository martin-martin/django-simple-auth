import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ApiCallForm


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = UserCreationForm(data=request.POST)
                signinform = AuthenticationForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')

            else:
                signinform = AuthenticationForm(data=request.POST)
                signupform = UserCreationForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')

        else:
            signupform = UserCreationForm()
            signinform = AuthenticationForm()

    return render(request, 'frontpage.html', {'signupform': signupform,
                                              'signinform': signinform})


@login_required
def signout(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    if request.method == 'POST':
        apiform = ApiCallForm(data=request.POST)
        if apiform.is_valid():
            base_URL = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key="
            key = apiform.cleaned_data['key']
            response = requests.get(base_URL + key)
            data = response.json()
    else:
        data = {}
    apiform = ApiCallForm()
    return render(request, 'profile.html', {'apiform': apiform, 'data': data})
