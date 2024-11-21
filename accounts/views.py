from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            # user_details = User.objects.get(username=username)
            user = authenticate(
                request, username=username, password=password
            )  # Check the username and password
            if user is not None:
                login(request, user)  # Login the user and return Http response.
                return HttpResponse("Login Success")
            else:
                return render(request, "login.html", {"message": "Invalid Credentials"})
        except ObjectDoesNotExist:
            return render(request, "login.html", {"message": "User does not exist"})

    context = {}
    return render(request, "login.html", context=context)


@require_POST
def logout_view(request):
    logout(request)
    if request.headers.get("HX-Request"):
        return HttpResponse(status=200, headers={"HX-Redirect": reverse("login")})
    return redirect("login")
