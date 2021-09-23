from rest_framework import viewsets
from .models import Article, SnapshotFile, VideoFile
from .serializers import ArticleSerializer, SnapshotFileSerializer, VideoFileSerializer
from .paginations import ArticlePageNumberPagination, SnapshotFilePageNumberPagination, VideoFilePageNumberPagination

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePageNumberPagination
    # pagination_class = None # 페이지네이션 안쓰려면 None으로

class SnapshotViewSet(viewsets.ModelViewSet):
    queryset = SnapshotFile.objects.all()
    serializer_class = SnapshotFileSerializer
    pagination_class = SnapshotFilePageNumberPagination

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerializer
    pagination_class = VideoFilePageNumberPagination
