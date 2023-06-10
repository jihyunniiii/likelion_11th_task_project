from django.shortcuts import get_object_or_404, render
from main.models import User

# Create your views here.

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'user/mypage.html', {'user': user})