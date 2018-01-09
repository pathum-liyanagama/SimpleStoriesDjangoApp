from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from .models import Story, Rating
from django.urls import resolve

client = Client()


class SmallTest(TestCase):
    """
    This test is for makesure tests are working fine.

    """

    def test_test_works(self):
        self.assertEqual(1 + 1 == 3, False)
        self.assertEqual(1 + 1 == 2, True)


class URLTest(TestCase):
    """
    To test the urls are working as intended
    """

    def setUp(self):
        Story.objects.create(title="Test title", content="Test content for a story")
        Rating.objects.create(story_id=1, value=5)

    def test_app_urls(self):
        resolver = resolve('/stories/')
        self.assertEqual(resolver.view_name, 'stories:index')

        resolver = resolve('/story/1')
        self.assertEqual(resolver.view_name, 'stories:story')

        rating = Rating.objects.get(pk=1)
        self.assertEqual(rating.value, 5)

        resolver = resolve('/story/1/ratings')
        self.assertEqual(resolver.view_name, 'stories:ratings')


class ModelTest(TestCase):
    """
    This will test the models

    """

    def setUp(self):
        Story.objects.create(title="Test title", content="Test content for a story")
        Rating.objects.create(story_id=1, value=5)

    def test_story_model(self):
        story = Story.objects.get(pk=1)
        self.assertEqual(story.title, "Test title")
        self.assertEqual(story.content, "Test content for a story")

    def test_rating_model(self):
        rating = Rating.objects.get(pk=1)
        self.assertEqual(rating.value, 5)
        self.assertEqual(rating.story_id, 1)


class FunctionalityTest(TestCase):
    """
    This will test the basic functionality of the app
    """

    def setUp(self):
        for i in range(6):
            Story.objects.create(title="Test title %s" % i,
                                 content="Test content for a story %s" % i)

    def test_for_retrieve_latest_stories(self):
        latest_stories = Story.objects.order_by('-created_at')[:5]
        self.assertEqual(latest_stories[0].title, "Test title 5")
        self.assertEqual(latest_stories[4].title, "Test title 1")

