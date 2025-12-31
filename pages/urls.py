from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name = "home"),
    path("signup/", views.SignUpView.as_view(), name = "signup"),
    path("contact/", views.contact_pages_views, name = "contact"),
    path("apropos/", views.apropos_pages_views, name = "apropos"),
    path("messages/", views.MessageListView.as_view(), name = "messages"),
]
