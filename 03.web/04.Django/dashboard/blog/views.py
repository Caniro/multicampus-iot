from django.views.generic import ListView, DetailView, \
        CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Post
from accounts.views import OwnerOnlyMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
