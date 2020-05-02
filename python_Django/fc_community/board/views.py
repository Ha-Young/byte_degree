from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards':boards})


def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # get user
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = request.POST.get('title', None)
            board.contents = request.POST.get('contents', None)
            board.writer = fcuser
            board.save()

            return redirect('../list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form':form})
