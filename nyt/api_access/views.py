from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
