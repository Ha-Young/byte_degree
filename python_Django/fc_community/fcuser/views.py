from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse("Home!")


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(email, password)

        res_data = {}
        if not (email and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            fcuser = Fcuser.objects.get(email=email)

            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, 'login.html', res_data)


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
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
