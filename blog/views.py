from django.urls import reverse   # importing url
from .models import Category, Post, Comment
from django.db.models import Count, Q  # for category search
from .forms import CommentForm
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)  # basic to render
from django.http import (
    HttpResponseRedirect,
    JsonResponse,
)  # Json need for ajax to likes
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.views import generic, View
from django.views.generic import TemplateView
# from django.views.generic.edit import UpdateView
# from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt  # need for ajax to likes
# from django.core.exceptions import ObjectDoesNotExist  # need for ajax to likes
from django.core.paginator import Paginator
from django.utils import timezone


class home_view(TemplateView):
    template_name = 'blog/home.html'


# View for class Post with category search, paginator,postlikes
def blog_index(request):
    search_query = request.GET.get('q', '')
    category_slug = request.GET.get('category', 'all')
    posts = Post.objects.filter(status=1).exclude(
        categories__slug='coursematerial'
    )

    if category_slug != 'all':
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(categories=category)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(excerpt__icontains=search_query)
        )

    # count of likes and comments to blogindex
    posts = posts.annotate(
        likes_count=Count('likes'), comments_count=Count('comments')
    )

    # paginator with 6 posts per side
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.exclude(slug='coursematerial')

    user_liked_posts = (
        set(request.user.like_post.values_list('id', flat=True))
        if request.user.is_authenticated
        else set()
    )

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "query": search_query,
        "current_category": category if category_slug != 'all' else None,
        "is_paginated": page_obj.has_other_pages(),
        'user_liked_posts': user_liked_posts,
    }

    return render(request, "blog/index.html", context)


# blogpost with comments, count of likes and comment


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    number_of_likes = post.likes.count()

    # Determine if the current user has liked the post
    post_is_liked = (
        request.user.is_authenticated
        and post.likes.filter(id=request.user.id).exists()
    )

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
                request,
                messages.SUCCESS,
                'Comment created and awaiting approval',
            )
            return HttpResponseRedirect(
                reverse('post_detail', args=[slug]) + "#comments"
            )

    return render(request, "blog/detail.html", context)


# like/unlike post


@require_POST
def like_post(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse(
            {'error': 'You must be logged in to like a post.'}, status=403
        )

    post = get_object_or_404(Post, id=post_id)
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return JsonResponse(
        {'likes_count': post.likes.count(), 'is_liked': is_liked}
    )

    # Display blog posts filtered by category name


def blog_category(request, category_slug):

    if category_slug == 'all':
        posts = Post.objects.filter(status=1).order_by('-created_on')
        # current_category = None
    else:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(categories=category, status=1).order_by(
            '-created_on'
        )
        # current_category = category

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    get_params = request.GET.copy()
    if 'page' in get_params:
        del get_params['page']
    querystring = get_params.urlencode()

    # categories = Category.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,
            'categories': Category.objects.all(),
            'current_category': category,
            'is_paginated': page_obj.has_other_pages(),
            'querystring': querystring,
        },
    )


# searchfield for categories


def category_search(request):
    query = request.GET.get('q')
    categories = Category.objects.filter(name__icontains=query)
    # paginator = Paginator(categories, 6)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    get_params = request.GET.copy()
    if 'page' in get_params:
        del get_params['page']
    # querystring = get_params.urlencode()

    return render(
        request,
        'blog/category_search.html',
        {
            'categories': categories,
            'query': query,
        },
    )


# login check on course page


@login_required
def course_detail(request, slug):
    course = get_object_or_404(Post, slug=slug, is_course_material=True)

    return render(request, 'courses/courses_detail.html', {'course': course})


# index for course material


def courses_view(request):
    courses = Post.objects.filter(is_course_material=True, status=1)
    logged_in = request.user.is_authenticated

    return render(
        request,
        'courses/courses.html',
        {
            'courses': courses,
            'logged_in': logged_in,
        },
    )


# comment edits with update and hidden form


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
            comment.updated_on = timezone.now()
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return HttpResponseRedirect(
                reverse('post_detail', args=[slug]) + f"#comment-{comment_id}"
            )
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request, "post_detail", {'comment_form': comment_form, 'post': post}
    )


# delete comment


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    # queryset = Post.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(
        reverse('post_detail', args=[slug]) + '#comments'
    )


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/signup.html', {'form': form})
    else:

        form = UserCreationForm()
        return render(request, 'account/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'},
            )

    return render(request, 'login.html')
