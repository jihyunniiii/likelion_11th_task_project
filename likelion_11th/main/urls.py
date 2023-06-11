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
    path('delete/<int:id>', delete, name="delete"),
    path('commentdelete/<int:postid>/<int:commentid>', commentdelete, name="commentdelete"),
    path('likes/<int:post_id>', likes, name="likes"),
]