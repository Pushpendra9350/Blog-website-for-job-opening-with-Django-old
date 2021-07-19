from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import( 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
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
        "posts":Post.objects.all()
    }
    return render(request, 'blogapp/home.html',context,status=201,)


class PostListView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class PostDetailsView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title","content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title","content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostListUserView(ListView):
    model = Post
    template_name = 'blogapp/post_per_user.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

def about(request):
    return render(request, 'blogapp/about.html')