import pytest

from core.db.models import PublishStateOptions
from videos.models import Video


@pytest.fixture()
def create_video():
    obj_a = Video.objects.create(title='this is my title', video_id='abc')
    obj_b = Video.objects.create(title='this is my title', state=PublishStateOptions.PUBLISH ,video_id='abcdefg')
    return obj_a, obj_b