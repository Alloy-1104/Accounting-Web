from django.urls import path
from .views import IndexView, LoginView, RegisterView, PaymentsView

urlpatterns = [
  path("", IndexView.as_view()),
  path("login/", LoginView.as_view()),
  path("register/", RegisterView.as_view()),
  path("payments/", PaymentsView.as_view()),
]
