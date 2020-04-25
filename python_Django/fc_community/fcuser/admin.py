from django.contrib import admin
from .models import Fcuser

# Register your models here.

# 관리자페이지에 Fcuser 등록하고 관리할 수 있게 하기.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'registered_dttm') # 리스트로 보이게 하기.

admin.site.register(Fcuser, FcuserAdmin)