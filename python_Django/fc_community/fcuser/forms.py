from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput,
                            max_length=32, label="이메일")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleanned_data = super().clean()
        email = cleanned_data.get('email')
        password = cleanned_data.get('password')

        if email and password:
            fcuser = Fcuser.objects.get(email=email)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
