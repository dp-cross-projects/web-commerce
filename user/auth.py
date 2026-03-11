from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

# Let the user register
def signup(request):
    # If POST method used, then create a user
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
            except IntegrityError:
                return render(request, 'user/signup.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
            })      
        else:
            return render(request, 'user/signup.html', {
                'form': UserCreationForm,
                'error': "Passwords did not match"
            })        
        # Redirect to Home
        return redirect('/')
    
    # If other method used, then render the
    # signup form
    else:
        return render(request, 'user/signup.html',{
            'form':UserCreationForm
        })

# Let the user signin
def signin(request):
    # If POST method used, then authenticate
    if request.method == 'POST':
        # Compare username and password received
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        # If credentials are wrong, then display
        # error to user
        if user is None:
            return render(request, 'user/signin.html', {
                'form': AuthenticationForm,
                'error': 'Bad Credentials'
            })
        
        # Save session cookie from Django to user browser
        login(request, user)

        # Redirect to Home
        return redirect('/')
    
    # If other method used, then render the login form
    else:
        return render(request, 'user/signin.html', {
            'form':AuthenticationForm
        })

# Let the user logout
def signout(request):

    # Delete the session cookie from browser
    logout(request)

    # Redirect to Home
    return redirect('/')


