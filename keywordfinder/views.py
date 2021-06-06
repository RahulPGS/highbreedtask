from django.shortcuts import render
from django.http import JsonResponse
from .forms import URLKeywordform
from .models import URLKeywords
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import json
import numpy as np
from django.conf import settings

# Create your views here.

"""

IMPORTANT NOTE:
    Find the Chrome version you are using and set its driver path as CHROME_DRIVER_PATH in settings.py.
    The above is required for the selenium to work.

"""

"""
In this view.py we will take an URL and then fetch the meta elements content from the keywords, description and \
og:description meta tags.

We are using JsonResponse to make the API as this is a simple app which just takes URL and returns the Keyword details.

HANDLING JAVASCRIPT NEEDED WEB PAGES:
    We will be using Selenium package to get the content of the web page from the URL as the web pages may rely on\
    Javascript to load their page content.

    NOTE:
        So make sure to set the chrome driver path of your chrome version as CHROME_DRIVER_PATH in settings.py

URL PATTERN VALIDATION:
    We will also validate the URL pattern in both Frontend(in JQuery) and backend(in the below code)

HEADER OPTIONS FOR SELENIUM:
    Then if the URL pattern is valid we set some header options to selenium to work in background.
    
    We will also add an experimental_option enable automation as it may help us to avoid the TOO Many Requests 429 error.

GETTING CONTENT:   
    And then we will try to access the url and get its content using Selenium.

HTML PARSER:
    If the content is fetched successfully then we will pass it to beautifulsoup to get the html parser and then use\
    to get the required elements.

HANDLING UNAVAILABLE CONTENT:
    If any of the meta content is not found we will set it to False to let the JQuery in the front end know that the\
    data is not available.

RECOMMENDED URLS AND KEYWORDS:
    We will also get the recommended keywords and urls from the existing model objects.

KEYWORD TRIMMING:
    We will trimming the unnecessary white spaces from the keywords.
    
HANDLING EXCEPTIONS:
    If an error occurs the success key in the JsonResponse will be set to False so that the JQuery will know that the\
    fetching failed and so that it should handle the error. The error information will also be sent along with it.

"""


def main(res):
    return render(res, 'findkeywords.html', {'form': URLKeywordform()})


def get_keywords(res):
    if res.method == 'POST':
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        url = res.POST['url']
        if not regex.search(url):
            return JsonResponse(data={'success': False, 'error': 'Enter a valid url'}, safe=False)
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            browser = webdriver.Chrome(settings.CHROME_DRIVER_PATH, options=options)
        except Exceprion as e:
            return JsonResponse(
                data={'success': False, 'error': 'An error occured with your chrome driver', 'detailed_error': str(e)},
                safe=False)
        try:
            browser.get(url)
        except Exception as e:
            print(str(e))
            return JsonResponse(data={'success': False, 'error': 'Unable to access the url'},
                                safe=False)
        try:
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            keywords = soup.find("meta", attrs={'name': 'keywords'})
            keywords = keywords['content'].split(',') if keywords else False
            description = soup.find("meta", attrs={'name': 'description'})
            description = description['content'] if description else False
            og_description = soup.find("meta", property="og:description")
            og_description = og_description['content'] if og_description else False
            recommended_keywords = []
            recommended_urls = []
            keywords = [keyword.replace(" ", '') for keyword in keywords] if keywords else False
            if keywords:
                for url_obj in URLKeywords.objects.all():
                    if url_obj.url == url:
                        continue
                    url_keywords = json.loads(url_obj.keywords)
                    if url_keywords:
                        if len(np.intersect1d(url_keywords, keywords)) > 3:
                            recommended_keywords += list(np.setdiff1d(url_keywords, keywords))
                            recommended_urls.append(url_obj.url)
            try:
                url_obj = URLKeywords.objects.get(url=url)
            except URLKeywords.DoesNotExist:
                url_obj = URLKeywords()
                url_obj.url = url
            url_obj.keywords = json.dumps(keywords)
            url_obj.description = description
            url_obj.og_description = og_description
            url_obj.save()
            recommended_keywords = recommended_keywords if recommended_keywords else False
            recommended_urls = recommended_urls if recommended_urls else False
            return JsonResponse(
                data={'keywords': keywords, 'description': description, 'ogdescription': og_description,
                      'success': True, 'recommended_keywords': recommended_keywords,
                      'recommended_urls': recommended_urls}, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse(data={'success': False, 'error': 'Enter valid URL'}, safe=False)
