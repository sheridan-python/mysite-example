import pytest

pytestmark = pytest.mark.django_db


def test_published_posts_only_returns_those_with_published_status():
    assert False
