from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

#This returns how post will be printed out
  def __str__(self):
    return self.title

#to redirect user after they post a blog. Import reverse
  def get_absolute_url(self):
      return reverse("post-detail", kwargs={"pk": self.pk})
  
