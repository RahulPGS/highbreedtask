from django.test import TestCase, Client
from django.urls import reverse
import json


# python manage.py test appsearcher

def assertJsonIsIn(actual_one, args):
    for arg in args:
        if json.dumps(arg) == actual_one:
            return True
    return False


class TestView(TestCase):

    def test_main(self):

        client = Client()

        response = client.get(reverse('appsearcher_main'))

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'appsearch.html')

    def test_search_app_store(self):
        client = Client()

        app_store_response = client.get(reverse('search_app_store', args=('__', 100)))

        self.assertEquals(app_store_response.status_code, 200)

        self.assertJSONEqual(
            str(app_store_response.content, encoding='utf8'),
            {'success': False, 'error': 'Enter a valid name'}
        )

        app_store_response_valid_name_id_pattern = client.get(reverse('search_app_store', args=('name', 55)))

        self.assertEquals(app_store_response_valid_name_id_pattern.status_code, 200)

        self.assertTrue(assertJsonIsIn(
            str(app_store_response_valid_name_id_pattern.content, encoding='utf8'), [{"success": False, "error": "There is a problem with the URL"},
               {'success': False, 'error': 'Check your internet connection and try again'}]))

        app_store_response_valid_name_id = client.get(
            reverse('search_app_store', args=('spotify-discover-new-music', 324684580)))

        self.assertEquals(app_store_response_valid_name_id.status_code, 200)

    def test_search_play_store(self):
        client = Client()

        play_store_response = client.get(reverse('search_play_store', args=('package_name',)))

        self.assertEquals(play_store_response.status_code, 200)

        self.assertJSONEqual(
            str(play_store_response.content, encoding='utf8'),
            {'success': False, 'error': 'Enter a valid package name'}
        )

        play_store_response_valid_package_pattern = client.get(
            reverse('search_play_store', args=('valid.test.pattern',)))

        self.assertEquals(play_store_response_valid_package_pattern.status_code, 200)

        self.assertTrue(
            assertJsonIsIn(str(play_store_response_valid_package_pattern.content, encoding='utf8'),
            [{"success": False, "error": "There is a problem with the URL"},
             {'success': False, 'error': 'Check your internet connection and try again'}]
        ))

        play_store_response_valid_package_name = client.get(
            reverse('search_play_store', args=('com.instagram.android',)))

        self.assertEquals(play_store_response_valid_package_name.status_code, 200)
