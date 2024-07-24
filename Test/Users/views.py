from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'goals/index.html')  # Render the index.html template

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Goals:goal_list')
    else:
        form = RegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Goals:goal_list')
    else:
        form = LoginForm()
    return render(request, 'Users/login.html', {'form': form})
from django.shortcuts import render



def contact(request):
    return render(request, 'Goals/contact.html')
