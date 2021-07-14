from django.shortcuts import render
# Create your views here.

posts=[
    {
        "author": "Pushpendra Kumar",
        "publish_date":"18/02/1998",
        "title":"this is a title",
        "content":"this is a descritption"
    },
    {
        "author": "Pushpendra Kumar",
        "publish_date":"18/02/1998",
        "title":"this is a second title",
        "content":"this is a second descritption"
    }
]

def home(request):
    context = {
        "posts":posts
    }
    return render(request, 'blogapp/home.html',context,status=201,)

def about(request):
    return render(request, 'blogapp/about.html')