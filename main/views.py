from django.shortcuts import render

from rest_framework import generics, viewsets, permissions

from .service import Pagination
from .serializers import (NewsSerializer,
                          RubricsSerializer,
                          MusicSerializer,
                          ImagesSerializer,
                          TextsSerializer,
                          CommentsCreateSerializer,
                          NewsDetailSerializer,
                          TextsDetailSerializer,
                          ImagesDetailSerializer)
from .models import News, Rubrics, Music, Images, Texts, Comments
# Create your views here.


class LolMixin(viewsets.ReadOnlyModelViewSet):
    queryset = None
    pagination_class = Pagination
    serializer_list = None
    serializers_retrieve = None

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_list
        elif self.action == 'retrieve':
            return self.serializers_retrieve

    # def get_permissions(self):
    #     if self.action == 'retrieve' or self.action == 'create':
    #         permissions_classes = [permissions.IsAuthenticated]
    #     else:
    #         permissions_classes = []
    #     return [permission() for permission in permissions_classes]


class NewsView(LolMixin):
    queryset = News.objects.all()
    serializer_list = NewsSerializer
    serializers_retrieve = NewsDetailSerializer


class NewsCreateView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer


class VideosView(viewsets.ReadOnlyModelViewSet):
    queryset = Rubrics.objects.all()
    serializer_class = RubricsSerializer


class MusicView(viewsets.ReadOnlyModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class ImagesView(LolMixin):
    queryset = Images.objects.all()
    serializer_list = ImagesSerializer
    serializers_retrieve = ImagesDetailSerializer


class ImagesCreateView(viewsets.ModelViewSet):
    serializer_class = ImagesSerializer


class TextsView(LolMixin):
    queryset = Texts.objects.all()
    serializer_list = TextsSerializer
    serializers_retrieve = TextsDetailSerializer
 

class TextsCreateView(viewsets.ModelViewSet):
    serializer_class = TextsSerializer


class CommentsCreateView(viewsets.ModelViewSet):
    model = Comments
    serializer_class = CommentsCreateSerializer


