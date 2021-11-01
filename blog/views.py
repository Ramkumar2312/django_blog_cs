from django.shortcuts import render
from .models import Post
# Create your views here.
posts = [
    {
        'title': 'The first post',
        'author': 'ted lasso',
        'content': 'welcome to the blog world',
        'date_posted': 'september 21 , 1995'
    },
    {
        'title': 'second update',
        'author': 'dwight schrute',
        'content': 'welcome to dunder mifflin',
        'date_posted': 'february 23, 2002'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'The about page'})

