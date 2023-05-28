from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
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
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/postdetail.html', {
            'post':post,
            'comments':comments,
        })
    elif request.method == "POST":
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        return redirect('main:postdetailpage', id)

def create(request):
    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.pub_date = timezone.now()
        new_post.body = request.POST['body']
        new_post.feedback = request.POST['feedback']
        new_post.good_point = request.POST['good_point']
        new_post.image = request.FILES.get('image')

        new_post.save()

        return redirect('main:postdetailpage', new_post.id)
    else:
        return redirect('accounts:login')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_post})

def update(request, id):
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user == update_post.writer:
            update_post.title = request.POST['title']
            update_post.pub_date = timezone.now()
            update_post.body = request.POST['body']
            update_post.feedback = request.POST['feedback']
            update_post.good_point = request.POST['good_point']
            if request.FILES.get('image') != None:
                update_post.image = request.FILES.get('image')

            update_post.save()
            return redirect('main:postdetailpage', update_post.id)
    return redirect('accounts:login')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:boardpage')

def commentdelete(request, commentid, postid):
    delete_comment = Comment.objects.get(id=commentid)
    delete_comment.delete()
    return redirect('main:postdetailpage', postid)