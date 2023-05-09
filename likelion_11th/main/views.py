from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def mypage(request):
    return render(request, 'main/mypage.html')

def repopage(request):
    return render(request, 'main/repopage.html')

def boardpage(request):
    posts = Post.objects.all()
    return render(request, 'main/boardpage.html', {'posts':posts})

def newpostpage(request):
    return render(request, 'main/newpostpage.html')

def postdetailpage(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/postdetail.html', {'post':post})

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.feedback = request.POST['feedback']
    new_post.good_point = request.POST['good_point']

    new_post.save()

    return redirect('main:postdetailpage', new_post.id)