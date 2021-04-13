from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view({'get': 'list'})),
    path('news/create/', views.NewsCreateView.as_view({'post': 'create'})),
    path('videos/', views.VideosView.as_view({'get': 'list'})),
    path('music/', views.MusicView.as_view({'get': 'list'})),
    path('images/', views.ImagesView.as_view({"get": 'list'})),
    path('images/create/', views.ImagesCreateView.as_view({'post': 'create'})),
    path('texts/', views.TextsView.as_view({'get': 'list'})),
    path('news/<int:pk>/', views.NewsView.as_view({'get': 'retrieve'})),
    path('images/<int:pk>/', views.ImagesView.as_view({"get": 'retrieve'})),
    path('texts/<int:pk>/', views.TextsView.as_view({'get': 'retrieve'})),
    path('texts/create/', views.TextsCreateView.as_view({'post': 'create'})),
    path('comments/create/', views.CommentsCreateView.as_view({'post': 'create'})),
]
