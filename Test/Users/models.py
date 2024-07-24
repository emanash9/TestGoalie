from django.db import models
from django.contrib.auth.models import User

class Contribution(models.Model):
    # Your fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contributions')  # Unique related_name
