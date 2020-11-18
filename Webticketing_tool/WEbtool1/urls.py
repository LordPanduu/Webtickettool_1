from django.urls import path
from . import views
urlpatterns = {
    path('', views.hi, name="home-page"),
    path('login', views.login, name="login-page"),
    path("dashboard", views.dashboard, name="dashboard-page"),
}
