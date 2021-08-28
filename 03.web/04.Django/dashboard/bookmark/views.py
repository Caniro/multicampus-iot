from typing import List
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, \
        CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.views import OwnerOnlyMixin

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    # form 클래스에서 사용할 필드 (form의 요소)
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    # post 요청 시 form의 유효성 검사 통과가 통과되면 호출되는 함수
    def form_valid(self, form):
        # form.instance : 폼 정보를 기반으로 생성된 모델 인스턴스
        form.instance.owner = self.request.user
        
        # form.instance를 DB에 저장하고, success_url 주소로 리다이렉트
        return super().form_valid(form)

class BookmarkChangeListView(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:change')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:change')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
