from django.contrib import admin

from videos.models.video_proxy import VideoAllProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'state', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy

admin.site.register(VideoAllProxy, VideoAllAdmin)