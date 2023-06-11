from django.urls import path
from .views import *

app_name = "user"
urlpatterns = [
    path('usermypage/<int:id>', mypage, name="mypage"),
    path('follow/<int:id>', follow, name="follow"),
]