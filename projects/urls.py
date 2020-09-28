from django.urls import path
from projects import views


urlpatterns = [
    path('myprojects/', views.UserProjects.as_view())

]
