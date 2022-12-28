from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)

class PostListView(ListView):
  model = Post
  template_name = "blog/home.html"
  context_object_name = 'posts' # Tells ListView what variable to loop over
  ordering = ['-date_posted']
  paginate_by = 5 #Allows user to see post by pages

class UserPostListView(ListView):
  model = Post
  template_name = "blog/user_posts.html"
  context_object_name = 'posts' # Tells ListView what variable to loop over
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

# User can click to get detail of a blog post
class PostDetailView(DetailView):
  model = Post

#To allow user to submit a blog post. 
class PostCreatelView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']

#Override the form_valid method. Sets author to current logged in user
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


# LoginRequiredMixin would redirect user to the login in page if they are not logged in
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

#With UserPassesTestMixin, this will forbid user from updating someone else's post. users will be redirected to 403 Forbidden page
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

# Allows users to delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})