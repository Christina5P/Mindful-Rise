from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Model for blogpost with fields for unique title,author,content,
    created, modified, many categories, draft or published,
    short excerpt, likes
    """

    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    featured_image = CloudinaryField('image', blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        "category", related_name="posts"
    )  # to assign many categories to many posts
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(
        blank=True
    )  
    likes = models.ManyToManyField(User, related_name='like_post', blank=True)
    is_course_material = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]


def number_of_likes(self):
    return self.likes.count()


class Comment(models.Model):
    """
    Model for Comments with fields for author,content,
    created, modified, many categories, link to blog post
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Category(models.Model):
    """
    slug field with category name for category list and Q-search
    """

    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

