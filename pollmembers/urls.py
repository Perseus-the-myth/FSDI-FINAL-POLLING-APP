
from django.urls import path
from pollmembers import views

urlpatterns = [
    path('', views.index),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.signout, name="signout"),
]
