from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from main.models import Todo


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {
                'error': True,
                'username': username,
                'password': password
            }

            return render(request, 'login.html', context)


class HomePage(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                "user": request.user,
                'todos': Todo.objects.filter(user=request.user)
            }
            return render(request, 'index.html', context)
        return redirect('login/')

    def post(self, request):
        if request.user.is_authenticated:
            title = request.POST.get('name')
            date = request.POST.get('date')
            status = request.POST.get('status')
            detail = request.POST.get('details')
            Todo.objects.create(title=title, deadline=date, status=status, detail=detail, user=request.user)

            return redirect('/')
        return redirect('login/')


class Edit(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            context = {
                "user": request.user,
                'todo': Todo.objects.get(user=request.user, id=id)
            }

            return render(request, 'edit.html', context)
        return redirect('login/')

    def post(self, request, id):
        if request.user.is_authenticated:
            title = request.POST.get('name')
            status = request.POST.get('status')
            detail = request.POST.get('details')
            task = Todo.objects.get(id=id)
            task.title = title
            task.status = status
            task.detail = detail
            task.save()

            return redirect('/')
        return redirect('login/')


def Logout(request):
    logout(request)
    return redirect('/login/')


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")

# class Edit(View):
#     def get(self,request, id):
#         context = {
#             'todo': Todo.objects.get(id=id)
#         }
#         return (id, context)
#
#     def post(self,request, id):
#         todo = Todo.objects.get(id=id)
#
#         todo_title = todo.title
#         content = todo.detail
#         deadline = todo.deadline


# def EditView(request, id):
#     if request.method == "GET":
#         context = {
#
#             "todo": Todo.objects.get(id=id)
#         }
#         return render(request, 'edit.html', context)
#     elif request.method == "POST":
#         pk = request.POST.get('pk')
#         title = request.POST.get("title")
#         content = request.POST.get("detail")
#         deadline = request.POST.get("deadline")
#
#         todo = Todo.objects.get(id=pk)
#
#         todo.title = title
#         todo.detail = content
#         todo.save()
#         return redirect('admin')
#
