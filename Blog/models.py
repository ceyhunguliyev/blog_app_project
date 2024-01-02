from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category Table
class CategoryTable(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="Blog")
    category = models.ForeignKey(CategoryTable, on_delete=models.PROTECT)
    published_date = models.DateField(auto_now_add=True)

    STATUS_CHOICES = (
        ("d", "Draft"),
        ("p", "Published")
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return f"{self.title - self.content - self.image - self.category - self.status}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_stamp = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.content - self.blog}"
    
class PostViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_views = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog - self.post_views}"

    
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.blog - self.likes}"