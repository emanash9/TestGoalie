from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from Test.Users.forms import RegisterForm  # Correct import for RegisterForm
from Test.Goals.forms import GoalForm  # Correct import for GoalForm
from django.shortcuts import render

def index(request):
    return render(request, 'goals/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form': form})
def contact(request):
    return render(request, 'contact.html')

def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('Goals:goal_detail', goal_id=goal.id)
    else:
        form = GoalForm()
    return render(request, 'Goals/create_goal.html', {'form': form})



