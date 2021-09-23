from rest_framework.pagination import PageNumberPagination

class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2

class SnapshotFilePageNumberPagination(PageNumberPagination):
    page_size = 10

class VideoFilePageNumberPagination(PageNumberPagination):
    page_size = 10
