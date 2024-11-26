from django.contrib import admin

from videos.models.video_proxy import VideoPublishedProxy


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    class Meta:
        model = VideoPublishedProxy
    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)