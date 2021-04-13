from rest_framework import serializers

from .models import News, Videos, Rubrics, Music, Images, Texts, Comments


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'video', 'image', 'author', 'source', 'published')


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('title','video')


class RubricsSerializer(serializers.ModelSerializer):
    videos = VideosSerializer(read_only=True, many=True)

    class Meta:
        model = Rubrics
        fields = ('name', 'videos')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('title', 'text', 'music', 'image', 'published')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('author', 'content', 'published')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id','title', 'image', 'published')


class ImagesDetailSerializer(serializers.ModelSerializer):
    comments_images = CommentsSerializer(many=True)

    class Meta:
        model = Images
        fields = ('id', 'title', 'image', 'published', 'comments_images')


class TextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texts
        fields = ('id', 'title', 'text', 'published')


class TextsDetailSerializer(serializers.ModelSerializer):
    comments_texts = CommentsSerializer(many=True)

    class Meta:
        model = Texts
        fields = ('id', 'title', 'text', 'published', 'comments_texts')


class CommentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    comments_news = CommentsSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'video', 'image', 'author', 'source', 'published', 'comments_news')
