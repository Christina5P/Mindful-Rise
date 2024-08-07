from django.shortcuts import render, get_object_or_404, redirect # basic to render
from django.db.models import Q   # for category search
from django.urls import path, include # importing url
from django.views import generic, View
from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Category, Post, Comment, Courses
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login 
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import CommentForm
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView, DeleteView
from .models import Comment, Home
from django.http import JsonResponse                        #need for ajax to likes
from django.views.decorators.csrf import csrf_exempt        #need for ajax to likes
from django.core.exceptions import ObjectDoesNotExist       #need for ajax to likes
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class home_view(TemplateView):
    template_name = 'blog/home.html'

def blog_index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    return render(request, "blog/index.html", {
        'page_obj': page_obj,
        'categories': categories,
        'is_paginated': page_obj.has_other_pages(),
    })

def blog_detail(request, slug):
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

    return render(request, "blog/detail.html", context)


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

def blog_category(request, category_slug):
    if category_slug == 'all':
        posts = Post.objects.filter(status=1).order_by('-created_on')
        current_category = None  # Ingen specifik kategori vald
    else:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(categories=category, status=1).order_by('-created_on')
        current_category = category

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Samla alla GET-parametrar för att inkludera dem i pagineringslänkar
    get_params = request.GET.copy()
    if 'page' in get_params:
        del get_params['page']
    querystring = get_params.urlencode()

    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': current_category,
        'is_paginated': page_obj.has_other_pages(),
        'querystring': querystring,
    })


def category_search(request):
    query = request.GET.get('q')
    categories = Category.objects.filter(name__icontains=query)
    paginator = Paginator(categories, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    get_params = request.GET.copy()
    if 'page' in get_params:
        del get_params['page']
    querystring = get_params.urlencode()

    return render(request, 'blog/category_search.html', {
        'categories': categories,
        'query': query,
    })

def courses_index(request):
    courses = Courses.objects.all().order_by("-created_on")
    context = {
        "courses": courses,
        'logged_in': request.user.is_authenticated,
        'login_url': '/login/',
        'signup_url': '/signup/'  
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
