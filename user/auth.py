from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def create_user(request):
    return render(request, 'user/signup.html',{
        'form':UserCreationForm
    })


def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'user/signin.html', {
                'form': AuthenticationForm,
                'error': 'Bad Credentials'
            })
        
        login(request, user)
        return redirect('/')
    
    else:
        return render(request, 'user/signin.html', {
            'form':AuthenticationForm
        })

def signout(request):
    logout(request)
    return redirect('/')


