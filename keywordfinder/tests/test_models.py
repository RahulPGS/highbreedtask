from django.test import TestCase
from keywordfinder.models import URLKeywords


# python manage.py test keywordfinder

class TestModels(TestCase):

    def setUp(self):
        self.url_keywords = URLKeywords.objects.create(
            url='http://sometesturl.whichdoesnt.exist',
            keywords='keyword1,keyword2,keyword3',
            description='Some very long description',
            og_description='Some very long og_description'
        )

    def test_url_keywords(self):
        self.assertEquals(str(self.url_keywords).strip(), """
                url: http://sometesturl.whichdoesnt.exist
                keywords: ['keyword1', 'keyword2', 'keyword3']
                description: Some very long description
                og_description: Some very long og_description
                """.strip())

    def test_url_keywords_update(self):
        self.url_keywords.keywords = 'keyword1,keyword2,keyword3,keyword4'
        self.url_keywords.save()

        self.assertEquals(str(self.url_keywords).strip(),  """
                url: http://sometesturl.whichdoesnt.exist
                keywords: ['keyword1', 'keyword2', 'keyword3', 'keyword4']
                description: Some very long description
                og_description: Some very long og_description
                """.strip())
