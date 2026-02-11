from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, TodoItem


class HomeView(View):
    def get(self, request):
        lists = TodoList.objects.all()
        return render(request, 'home.html', {'lists': lists})

    def post(self, request):
        if 'list_name' in request.POST:
            TodoList.objects.create(name=request.POST.get('list_name'))
        elif 'delete_list' in request.POST:
            TodoList.objects.filter(id=request.POST.get('delete_list')).delete()
        return redirect('/')

    
class TodoDetailView(View):

    def get(self, request, pk):
        todo_list = get_object_or_404(TodoList, id=pk)
        edit_item_id = request.GET.get('edit')
        return render(
            request,
            'todo_detail.html',
            {
                'list': todo_list,
                'edit_item_id': edit_item_id
            }
        )

    def post(self, request, pk):
        todo_list = get_object_or_404(TodoList, id=pk)

        # ADD ITEM
        if 'item_title' in request.POST:
            TodoItem.objects.create(
                title=request.POST.get('item_title'),
                todo_list=todo_list
            )

        # DELETE ITEM
        elif 'delete_item' in request.POST:
            TodoItem.objects.filter(
                id=request.POST.get('delete_item')
            ).delete()

        # UPDATE ITEM
        elif 'update_item' in request.POST:
            item_id = request.POST.get('update_item')
            new_title = request.POST.get('new_title')

            TodoItem.objects.filter(id=item_id).update(
                title=new_title
            )

        return redirect('todo-detail', pk=pk)

