from django.contrib import admin
from .models import Tag
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    # 리스트로 보이게 하기.
    list_display = ('name', 'registered_dttm')


admin.site.register(Tag, TagAdmin)
