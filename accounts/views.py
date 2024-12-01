from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django_htmx.http import retarget

from framework.views import HtmxHttpRequest


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("quiz:list")

    def form_invalid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        response = super().form_invalid(form)
        return retarget(response, "#login-form")


@require_POST
def logout_view(request: HtmxHttpRequest):
    logout(request)
    return HttpResponse(status=200, headers={"HX-Redirect": reverse("login")})
