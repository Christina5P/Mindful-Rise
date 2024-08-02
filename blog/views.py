from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import path, include
from django.views import generic, View
from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Category, Post, Comment, Courses
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import CommentForm
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView, DeleteView
from .models import Comment
from django.http import JsonResponse                        #need for ajax to likes
from django.views.decorators.csrf import csrf_exempt        #need for ajax to likes
from django.core.exceptions import ObjectDoesNotExist       #need for ajax to likes

# Create your views here.

class home_view(TemplateView):
    """
    Home page
    """
    template_name = 'blog/home.html'

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

def blog_index(request):
    """
    Display all blog posts ordered by creation date in descending order.
    Render from index.html
    """
    posts_list = Post.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(posts_list, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "is_paginated": paginator.num_pages > 1,
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

def blog_detail(request, slug):
    """
    Display details of a single blog post and its associated comments and likes
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    number_of_likes = post.likes.count()
    post_is_liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False

    context = {
        "post": post,
        "comments": comments,
        "number_of_likes": number_of_likes,
        "comment_count": comment_count,
        "post_is_liked": post_is_liked,
        "comment_form": CommentForm(),
    }

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        comment_form = CommentForm()
    return render(request, "blog/detail.html", context)

def signup_view(request):
    return render(request, 'account/login.html')


@csrf_exempt
def like_post(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    try:
        post = Post.objects.get(id=post_id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            result = {'status': 'unliked', 'likes_count': post.likes.count()}
        else:
            post.likes.add(request.user)
            result = {'status': 'liked', 'likes_count': post.likes.count()}
        return JsonResponse(result)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Post does not exist', 'post_id': post_id}, status=404)
    
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

def courses_index(request):
    courses = Courses.objects.all().order_by("-created_on")
    context = {
        "courses": courses,
    }
    return render(request, 'blog/courses.html', context)

def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {'comment_form': comment_form, 'post': post})

def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
