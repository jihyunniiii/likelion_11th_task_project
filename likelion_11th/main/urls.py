from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mypage, name="mypage"),
    path('repo/', repopage, name="repopage"),
    path('board/', boardpage, name="boardpage"),
    path('newpost/', newpostpage, name="newpostpage"),
    path('create/', create, name="create"),
    path('<int:id>', postdetailpage, name="postdetailpage"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
]