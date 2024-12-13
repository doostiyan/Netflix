import pytest
from django.utils import timezone
from django.utils.text import slugify

from core.db.models import PublishStateOptions
from videos.models import Video

@pytest.mark.django_db
class TestVideo:
    def test_slug_field(self, create_video):
        obj_a, _ = create_video
        title = obj_a.title
        test_slug = slugify(title)
        assert test_slug == obj_a.slug

    def test_slug_title(self, create_video):
        title = 'this is my title'
        qs = Video.objects.filter(title=title)
        assert qs.exists()
        assert qs.first().title == title

    def test_created_count(self, create_video):
        qs = Video.objects.all()
        assert qs.count() == 2


    def test_draft_case_count(self, create_video):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        assert qs.count() == 1


    def test_draft_case_is_published(self, create_video):
        obj = Video.objects.filter(state=PublishStateOptions.DRAFT).first()
        assert not obj.is_published

    def test_publish_case_count(self, create_video):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
                                            )
        assert published_qs.count() == 1
        assert published_qs.exists()

    def test_publish_case_is_published(self, create_video):
        obj = Video.objects.filter(state=PublishStateOptions.PUBLISH).first()
        assert obj.is_published


    def test_publish_manager(self, create_video):
        published_qs = Video.objects.all().published()
        published_qs_2 = Video.objects.published()
        assert published_qs.exists()
        assert published_qs.count() == published_qs_2.count()