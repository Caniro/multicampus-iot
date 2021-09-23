from rest_framework import serializers
from .models import Article, SnapshotFile, VideoFile

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ('id','title','content', 'reg_date','update_date') # 필드 설정
        exclude = []

class SnapshotFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapshotFile
        exclude = []

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        exclude = []
