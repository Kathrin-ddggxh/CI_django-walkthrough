from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    # takes http request from user
    # and returns http response that says hello
    # need to import HttpResponse from django.shortcuts 
    return render(request, 'todo/todo_list.html')
