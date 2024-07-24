# Test/Goals/utils.py

from .models import Contribution

def get_goal_progress(goal):
    total_contributed = Contribution.objects.filter(goal=goal).aggregate(Sum('amount'))['amount__sum'] or 0
    progress_percentage = (total_contributed / goal.target_amount) * 100
    return progress_percentage
