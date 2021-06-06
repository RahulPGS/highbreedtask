from django.test import TestCase, Client
from django.urls import reverse


# python manage.py test keywordfinder

class TestView(TestCase):

    def test_main(self):

        client = Client()

        response = client.get(reverse('keyword_finder_main'))

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'findkeywords.html')

    def test_get_keywords(self):

        client = Client()

        response_invalid_url_pattern = client.post(reverse('get_keywords'), {'url': 'some_invalid_url_pattern'})

        self.assertEquals(response_invalid_url_pattern.status_code, 200)

        self.assertJSONEqual(
            str(response_invalid_url_pattern.content, encoding='utf8'),
            {'success': False, 'error': 'Enter a valid url'}
        )

        response_invalid_url = client.post(reverse('get_keywords'), {'url': 'http://invalid.url.sbjwdjkcbjbf'})

        self.assertEquals(response_invalid_url.status_code, 200)

        self.assertJSONEqual(
            str(response_invalid_url.content, encoding='utf8'),
            {"success": False, "error": "Unable to access the url"}
        )

        response_valid_url = client.post(reverse('get_keywords'), {'url': 'https://stratz.com/'})

        self.assertEquals(response_valid_url.status_code, 200)