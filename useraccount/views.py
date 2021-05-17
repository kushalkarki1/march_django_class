from django.shortcuts import render, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from useraccount.forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


class UserLogin(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class UserSignupView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user:login")


def send_email_to_user(request):
    subject = "Testing Django Email"
    message = "Hello, we are testing our django email."
    from_email = "ytddash@gmail.com"
    recipient_list = ["officialtam01@gmail.com",]
    html_message = render_to_string("email.html", {"name": "Satyam"})
    val = send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return HttpResponse(val)
