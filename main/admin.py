from django.contrib import admin

# Register your models here.
from .models import News, Videos, Rubrics, Music, Images, Texts, Comments


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    list_display_links = ('id', 'title')
    inlines = [CommentsInline]

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    list_display_links = ('id', 'title')
    inlines = [CommentsInline]

@admin.register(Texts)
class TextsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    list_display_links = ('id', 'title')
    inlines = [CommentsInline]


admin.site.register(Videos)
admin.site.register(Rubrics)
admin.site.register(Music)
