from django.contrib import admin
from django.urls import path, include
from Test.Users import views as user_views
from Test.Goals import views as goals_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Goals/', include('Test.Goals.urls')),
    path('Users/', include('Test.Users.urls')),
    path('', user_views.index, name='index'),  # Root URL mapped to a view
    path('goal/<int:goal_id>/contributions/', goals_views.view_contributions, name='view_contributions'),
]
