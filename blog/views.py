from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from django.views import generic, View
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post, Comment
from django.urls import path, include
from django.contrib.auth.decorators import login_required


# Create your views here.

class PostList(generic.ListView):
    """
    A view to list all posts with status 'published'.
    Generic ListView is a standard view
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def blog_index(request):
    """
    Display all blog posts ordered by creation date in descending order.
    Render from index.html
    """
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }

    
@login_required
def post_like(request, pk):
    """
    Handle the liking and unliking of a blog post by the user.
    """
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

