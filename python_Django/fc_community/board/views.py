from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)
    
    return render(request, 'board_list.html', {'boards':boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')
        
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


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board':board})