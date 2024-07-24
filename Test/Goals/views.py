from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GoalForm, ContributionForm
from .models import Goal, Contribution
from .utils import get_goal_progress
from django.db.models import Sum
from decimal import Decimal




@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('Goals:goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/create_goal.html', {'form': form})


@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/goal_list.html', {'goals': goals})


@login_required

def goal_detail(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    return render(request, 'goals/goal_detail.html', {'goal': goal})


@login_required

# Test/Goals/views.py
def view_contributions(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    contributions = Contribution.objects.filter(goal=goal)

    # Calculate total contributed amount and ensure it's a Decimal
    total_contributed = contributions.aggregate(Sum('amount'))['amount__sum'] or 0
    total_contributed = Decimal(total_contributed)

    # Ensure goal.target_amount is a Decimal
    try:
        target_amount = Decimal(goal.target_amount)
    except (ValueError, TypeError):
        target_amount = Decimal('0.0')

    # Calculate progress percentage
    if target_amount > 0:
        progress_percentage = (total_contributed / target_amount) * 100
    else:
        progress_percentage = 0

    context = {
        'goal': goal,
        'contributions': contributions,
        'progress_percentage': progress_percentage,
    }

    return render(request, 'goals/view_contributions.html', context)

def add_contribution(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.goal = goal
            contribution.user = request.user
            contribution.save()
            # Check if the contribution is saved
            print(f"Saved contribution: {contribution}")
            return redirect('view_contributions', goal_id=goal.id)
    else:
        form = ContributionForm()
    return render(request, 'goals/add_contribution.html', {'goal': goal, 'form': form})


@login_required
def edit_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('Goals:goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/edit_goal.html', {'form': form, 'goal': goal})


@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('Goals:goal_list')
    return render(request, 'goals/confirm_delete.html', {'goal': goal})
