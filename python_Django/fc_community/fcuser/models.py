from django.db import models

# Create your models here.

# Fcuser Model 생성. verbose_name으로 관리자페이지에 한글나오게 하기.
class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=32,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now=True,
                                            verbose_name='등록시간')
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        # 관리자페이지에 한글명나오게하기
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'