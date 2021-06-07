from django.test import SimpleTestCase
from keywordfinder.forms import URLKeywordform


# python manage.py test keywordfinder


class TestForm(SimpleTestCase):

    def test_url_keywords_form_valid_data(self):

        form = URLKeywordform(data={
            'url': 'http://sometesturl.whichdoesnt.exist',
            'keywords': 'keyword1,keyword2,keyword3',
            'description': 'Some very long description',
            'og_description': 'Some very long og_description'
        })

        self.assertTrue(form.is_valid())

    def test_url_keywords_form_no_data(self):

        form = URLKeywordform(data={})

        self.assertFalse(form.is_valid())

        self.assertEquals(len(form.errors), 1)