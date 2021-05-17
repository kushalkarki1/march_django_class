from django.urls import path
from useraccount.views import UserLogin, UserSignupView, send_email_to_user

app_name = "user"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", UserSignupView.as_view(), name="register"),
    path("send-mail/", send_email_to_user, name="send-mail"),
]