from django.urls import path, re_path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
