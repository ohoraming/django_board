from django.shortcuts import redirect, render
from board.forms import BoardForm
from board.models import Board

# Create your views here.

def index(request):
    """
    첫 화면
    """
    board_list = Board.objects.all()
    context = {'board_list': board_list}
    return render(request, 'board/index.html', context)

def detail(request, board_id):
    """
    상세 화면
    """
    board_detail = Board.objects.get(board_id=board_id)
    context = { 'board': board_detail }
    return render(request, 'board/detail.html', context)

def create(request):
    """
    게시물 생성
    """
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('board:index')
    else:
        form = BoardForm()

    context = {'form': form}
    
    return render(request, 'board/form.html', context)

def update(request, board_id):
    """
    게시물 수정
    """
    board = Board.objects.get(board_id=board_id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board.save()
            return redirect('board:detail', board_id=board_id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'board/form.html', context)

def delete(request, board_id):
    """
    게시물 삭제
    """
    board = Board.objects.get(board_id=board_id)
    board.delete()

    return redirect('board:index')