# Generated by Django 3.0.5 on 2020-04-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=32, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='fcuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
