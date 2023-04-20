from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def mypage(request):
    return render(request, 'main/mypage.html')

def repopage(request):
    return render(request, 'main/repopage.html')

def boardpage(request):
    return render(request, 'main/boardpage.html')

def newpostpage(request):
    return render(request, 'main/newpostpage.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.feedback = request.POST['feedback']
    new_post.good_point = request.POST['good_point']

    new_post.save()

    return redirect('detail', new_post.id)