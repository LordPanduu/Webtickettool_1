from django.urls import path
from . import views
from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView
urlpatterns = [
    path('', TicketListView.as_view(), name="dashboard-page"),
   # path('login', views.login, name="login-page"),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name="Ticket_detail"),
    path('ticket/new/', TicketCreateView.as_view(), name="Ticket_create"),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name="Ticket_update"),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name="Ticket_delete"),
]
