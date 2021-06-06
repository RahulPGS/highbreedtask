from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appsearcher.views import get_app_details_from_app_store, get_app_details_from_play_store, search_app, main


# python manage.py test appsearcher

class TestUrls(SimpleTestCase):

    def test_main(self):
        url = reverse('appsearcher_main')
        self.assertEquals(resolve(url).func, main)

    def test_search_app_store(self):
        url = reverse('search_app_store', args=('name', 0))
        self.assertEquals(resolve(url).func, search_app)

    def test_search_play_store(self):
        url = reverse('search_play_store', args=('package_name',))
        self.assertEquals(resolve(url).func, search_app)
