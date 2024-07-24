from django.urls import path
from . import views

app_name = 'Goals'

urlpatterns = [
    path('create/', views.create_goal, name='create_goal'),
    path('goal-list/', views.goal_list, name='goal_list'),
    path('goal-detail/<int:goal_id>/', views.goal_detail, name='goal_detail'),
    path('goal-edit/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    path('goal-delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('goal/<int:goal_id>/contributions/', views.view_contributions, name='view_contributions'),

    path('goal/<int:goal_id>/add-contribution/', views.add_contribution, name='add_contribution'),
    path('goal/<int:goal_id>/contributions/', views.view_contributions, name='view_contributions'),
]
