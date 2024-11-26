from django.db.models.signals import pre_save

from core.db.receivers import publish_state_pre_save, slugify_pre_save
from videos.models.video import Video


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'


pre_save.connect(publish_state_pre_save, sender=Video)
pre_save.connect(slugify_pre_save, sender=Video)


pre_save.connect(publish_state_pre_save, sender=VideoAllProxy)
pre_save.connect(slugify_pre_save, sender=VideoAllProxy)


pre_save.connect(publish_state_pre_save, sender=VideoPublishedProxy)
pre_save.connect(slugify_pre_save, sender=VideoPublishedProxy)
