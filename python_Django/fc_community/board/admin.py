from django.contrib import admin
from .models import Board

# Register your models here.

# 관리자페이지에 Board 등록하고 관리할 수 있게 하기.


class BoardAdmin(admin.ModelAdmin):
    # 리스트로 보이게 하기.
    list_display = ('title', 'contents', 'writer', 'registered_dttm')


admin.site.register(Board, BoardAdmin)
