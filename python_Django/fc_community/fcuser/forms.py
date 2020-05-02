from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="사용자 이름", required=True,
        widget=forms.Textarea, max_length=32,
        error_messages={
            'required':'사용자이름을 입력해주십시오'
        })
    email = forms.EmailField(
        label="이메일",
        max_length=128,
        error_messages={
            'required':'이메일을 입력해주십시오'
        })
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput, max_length=64, 
        error_messages={
            'required':'비밀번호를 입력해주십시오'
        })
    re_password = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput, max_length=64,
        error_messages={
            'required':'비밀번호 확인을 입력해주십시오'
        })

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput,
        max_length=32, label="이메일",
        error_messages={
            'required': '이메일을 입력해주십시오'
        })
    password = forms.CharField(
        widget=forms.PasswordInput, label="비밀번호",
        error_messages={
        'required': '비밀번호를 입력해주십시오'
        })

    def clean(self):
        cleanned_data = super().clean()
        print(cleanned_data)
        email = cleanned_data.get('email')
        password = cleanned_data.get('password')
        
        print(email, password)

        if email and password:
            fcuser = Fcuser.objects.get(email=email)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.user_id = fcuser.id