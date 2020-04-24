from django.http import HttpResponse
from django.shortcuts import render
from .models import Fcuser

# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                email=email,
                password=password
            )

            fcuser.save()
        
        return render(request, 'register.html', res_data)