from django.test import SimpleTestCase
from django.urls import reverse, resolve
from keywordfinder.views import get_keywords, main


# python manage.py test keywordfinder

class TestUrls(SimpleTestCase):

    def test_main(self):

        url = reverse('keyword_finder_main')

        self.assertEquals(resolve(url).func, main)

    def test_get_keywords(self):

        url = reverse('get_keywords')

        self.assertEquals(resolve(url).func, get_keywords)