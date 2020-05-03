from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm, RegisterForm

# Create your views here.


def home(request):
    return render(request, 'home.html')
    
    
def logout(request):
    print("logout")
    print(request.session.get('user'))
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # session
            request.session['user'] = form.user_id
            return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == "POST":
        res_data = {}
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            re_password = request.POST.get('re_password', None)

            if password != re_password:
                res_data['error'] = '비밀번호가 다릅니다.'
                return render(request, 'register.html', res_data, {'form':form})
            else:
                fcuser = Fcuser(
                    username=username,
                    email=email,
                    password=make_password(password)
                )

                fcuser.save()

                form = LoginForm()
                return redirect('../login')
        else:
            return render(request, 'register.html', {'form':form})
            

        
