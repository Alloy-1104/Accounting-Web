from typing import Any
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = "index.html"

  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt["page_title"] = "ダッシュボード"
    return ctxt

class LoginView(TemplateView):
  template_name = "login.html"

class RegisterView(TemplateView):
  template_name = "register.html"

class PaymentsView(TemplateView):
  template_name = "payments.html"

  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt["page_title"] = "出納"
    return ctxt