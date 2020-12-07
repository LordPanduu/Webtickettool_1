from django.urls import path
from . import views
from .views import TicketListView
urlpatterns = {
    path('', views.hi, name="home-page"),
    path('login', views.login, name="login-page"),
    path("dashboard", TicketListView.as_view(), name="dashboard-page"),
}
