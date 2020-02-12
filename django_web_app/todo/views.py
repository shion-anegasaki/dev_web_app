from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm


def index(request):
    context = {
        'items': Todo.objects.all(),
        'form': TodoForm()}
    return render(request, 'todo/index.html', context)

def regist(request):
    form = TodoForm(request.POST)
    if not form.is_valid():
        # バリデーションエラー時の処理
        print(form.erros)
    else:
        # 入力に問題が無い時の処理
        todo = Todo(
            text=form.cleaned_data['text'],
            is_done=form.cleaned_data['is_done'])
        todo.save()
        return redirect('/todo')

