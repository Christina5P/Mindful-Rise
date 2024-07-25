from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import path, include
from django.views import generic, View
from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post, Comment, Courses
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


# Create your views here.

class home_view(TemplateView):
    """
    Home page
    """
    template_name = 'blog/home.html'

class PostList(generic.ListView):
    """
    A view to list all posts with status 'published'.
    Generic ListView is a standard view. Views in /blog
    """
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 2
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)


    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

        
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

def blog_index(request):
    """
    Display all blog posts ordered by creation date in descending order.
    Render from index.html
    """
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
    
def blog_category(request, category):
    """
    Display blog posts filtered by category name.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    """
    Display details of a single blog post and its associated comments and likes
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by("-created_on")
    #comment_count = post.comments.filter(approved=True).count()
    number_of_likes = post.likes.count()

    post_is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post_is_liked = True

    context = {
        "post": post,
        "comments": comments,
        "number_of_likes": number_of_likes,
        "post_is_liked": post_is_liked,
    }

    return render(
        request, 
    "blog/detail.html",
      {
        "post": post,
        "comments": comments,
        #"comment_count": comment_count,
        "comment_form": CommentForm()

    },
)

def category_search(request):
    """
    Search for categories based on a query string.
    """
    query = request.GET.get('q')
    if query:
        categories = Category.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        categories = Category.objects.all()
    
    context = {
        'categories': categories,
        'query': query,
    }
    return render(request, 'blog/category.html', context)

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


def courses_index(request):
    courses = Post.objects.all().order_by("-created_on")
    context = {
        "courses": courses,
    }
    return render(request, 'blog/courses.html', context)

