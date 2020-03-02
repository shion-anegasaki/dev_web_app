from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from dwa_common.models import Todo
from dwa_todo.forms import TodoForm


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

def detail(request, pk):
    form = TodoForm(request.POST)
    todo = Todo.objects.get(pk=pk)
    res = {}
    if todo:
        res = {
            'id': pk,
            'text': todo.text,
            'is_done': 1 if todo.is_done else 0}
    return JsonResponse(res)

def edit(request):
    pk = int(request.POST.get('todo_id'))
    text = request.POST.get('text', '')
    is_done = True if int(request.POST.get('is_done', 0)) > 0 else False

    form = TodoForm({'text': text, 'is_done': is_done})
    todo = Todo.objects.get(pk=pk)
    form.is_valid()

    if not form.is_valid() or not todo:
        print(form.errors)
    else:
        todo.text=form.cleaned_data['text']
        todo.is_done=form.cleaned_data['is_done']
        todo.save()
        return redirect('/todo')

def delete(request):
    pk = int(request.POST.get('todo_id'))
    todo = Todo.objects.get(pk=pk)

    if not todo:
        print('error')
    else:
        todo.delete()
        return redirect('/todo')