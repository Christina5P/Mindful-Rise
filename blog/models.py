from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

STATUS = ((0, "Draft"), (1, "Published"))

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
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("category", related_name="posts") #to assign many categories to many posts
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)     # to show short beginning from textfield
    featured_images= CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='like_post')
    anonymous_likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def number_of_likes(self):
        return self.likes.count()

class Category(models.Model):
    """
    Model for Categories with fields for category name, description,
    created, updated 
    """
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    
class Comment(models.Model):
    """
    Model for Comments with fields for author,content,
    created, modified, many categories, link to blog post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

   
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
  

class Courses(models.Model):
    """
    Model for courses with fields for unique title,author,content,
    created, modified, many categories, draft or published
    """
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField("Category", related_name="courses")
     
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
            return self.title
        
        
class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
