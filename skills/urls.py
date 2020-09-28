from django.urls import path
from skills import views


urlpatterns = [
    path('myskills/', views.UserSkills.as_view())

]
