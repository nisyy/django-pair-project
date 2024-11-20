from django.shortcuts import render
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all().order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'items': items})
