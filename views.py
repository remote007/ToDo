from django.shortcuts import render,redirect
from .models import Todo
from django.http import HttpResponse,HttpRequest
def list_todo_items(request):
    context = { 'todo_list' : Todo.objects.all()}
    #return HttpResponse(' from list_todo_items ')
    return render(request,'todo_list.html',context)
def insert_todo_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')
def delete_todo_item(request,todo_id):
    Todo.objects.filter(id=todo_id).delete()
    return redirect('/todos/list/')
