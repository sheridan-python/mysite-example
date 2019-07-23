from model_mommy import mommy
import pytest

from blog.models import Post

# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db


def test_published_posts_only_returns_those_with_published_status():
    # Create a published Post by setting the status to "published"
    published = mommy.make('blog.Post', status=Post.PUBLISHED)
    # Create a draft Post
    mommy.make('blog.Post', status=Post.DRAFT)

    # We expect only the "publised" object to be returned
    expected = [published]
    # Cast the result as a list so we can compare apples with apples!
    # Lists and querysets are of different types.
    result = list(Post.objects.published())

    assert result == expected


def test_draft_posts_only_returns_those_with_draft_status():
    draft = mommy.make('blog.Post', status=Post.DRAFT)
    mommy.make('blog.Post', status=Post.PUBLISHED)

    expected = [draft]
    result = list(Post.objects.drafts())

    assert result == expected
