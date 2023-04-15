from django.shortcuts import render

# Create your views here.

def mypage(request):
    return render(request, 'main/mypage.html')

def repopage(request):
    return render(request, 'main/repopage.html')

def boardpage(request):
    return render(request, 'main/boardpage.html')