from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.

"""

In this views.py we will take the required details of an app and fetch its details from its web page.

API
We are using JsonResponse to make the API as this is a simple app which just returns the app details. 

GETTING PAGE CONTENT
We will be using requests package as it is enough to get the content from the playstore and appstore web pages as they \
don't rely on Javascript to load the page content.

PARSING
Then we will get the content and pass it to beautifulsoup and get its html parser and then use it to find our required \
elements.

EXCEPTION HANDLING
While handling exceptions we will set the success in the JsonResponse to False to let the front end know that an error\
occurred and handle it.

If there are no errors then the success will be True and then the Jquery in the template can set the details of the app\
in the page.

PACKAGE_NAME_VALIDATION
Package name and name validations are also implemented in the frontend(in JQuery) and the backend(in the below code).
"""


def get_app_details_from_app_store(name, id):
    # name = 'spotify-discover-new-music'
    # id = '324684580'
    name_pattern = re.compile('([A-Za-z-])+')
    if name == '' or not name_pattern.search(name):
        return JsonResponse({'success': False, 'error': 'Enter a valid name'}, safe=False)
    try:
        link = f'https://apps.apple.com/in/app/{name}/id{id}'
        req_link = requests.get(link)
        req_link.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return JsonResponse({'success': False, 'error': 'There is a problem with the URL'},
                            safe=False)

    except requests.exceptions.ConnectionError as e:
        print(e)
        return JsonResponse(
            {'success': False, 'error': 'Check your internet connection and try again'},
            safe=False)
    try:
        soup = BeautifulSoup(req_link.content, 'html.parser')
        title = soup.find('h1', attrs={'class': 'product-header__title app-header__title'}).contents[0].strip()
        image = soup.find('source', attrs={'class': 'we-artwork__source'})['srcset'].split(' ', 1)[0]
        ratings = \
            soup.find('div', attrs={'class': 'we-customer-ratings__count small-hide medium-show'}).text.split(' ', 1)[
                0]
        rating = soup.find('span', attrs={'class': 'we-customer-ratings__averages__display'}).text
        description = soup.find('div', attrs={'class': 'section__description'}).div.div.p.text[:200]
        downloads = 'Unknown'
        developer = soup.find('dd', attrs={'class': 'information-list__item__definition'}).text.strip()
        return JsonResponse(
            data={'success': True, 'image': image, 'name': title, 'ratings': ratings, 'rating': rating,
                  'description': description,
                  'developer': developer, 'downloads': downloads, 'link': link}, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(
            {'success': False, 'error': 'Error while retrieving information from the URL'},
            safe=False)


def get_app_details_from_play_store(package_name):
    # package_name = 'com.imangi.templerun'
    package_name_pattern = re.compile('^([A-Za-z]{1}[A-Za-z\d_]*\.)+[A-Za-z][A-Za-z\d_]*$')
    if not package_name_pattern.search(package_name):
        return JsonResponse({'success': False, 'error': 'Enter a valid package name'}, safe=False)
    try:
        link = f'https://play.google.com/store/apps/details?id={package_name}'
        req_link = requests.get(link)
        req_link.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return JsonResponse({'success': False, 'error': 'There is a problem with the URL'},
                            safe=False)

    except requests.exceptions.ConnectionError as e:
        print(e)
        return JsonResponse(
            {'success': False, 'error': 'Check your internet connection and try again'},
            safe=False)
    try:
        soup = BeautifulSoup(req_link.content,
                             'html.parser')
        title = soup.find('h1', attrs={'itemprop': 'name'}).span.string
        ratings = soup.find('span', attrs={'class': 'AYi5wd TBRnV'}).span.string
        image = soup.find('div', attrs={'class': 'xSyT2c'}).img['src']
        description = soup.find('div', attrs={'itemprop': 'description'}).span.div.text[:200]
        rating = soup.find('div', attrs={'class': 'BHMmbe'}).text
        add_info = [div.find('span').div.span.text for div in soup.find('div', attrs={'class': 'IxB2fe'})]
        app_info_labels = [div.div.text for div in soup.find('div', attrs={'class': 'IxB2fe'})]
        downloads = add_info[app_info_labels.index('Installs')]
        developer = add_info[app_info_labels.index('Offered By')]
        return JsonResponse(
            data={'success': True, 'name': title, 'ratings': ratings, 'image': image, 'description': description,
                  'rating': rating, 'downloads': downloads, 'developer': developer, 'link': link},
            safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': 'App not found with given details'},
                            safe=False)


def search_app(res, name, id=None):
    if id:
        return get_app_details_from_app_store(name, id)
    return get_app_details_from_play_store(name)


def main(res):
    return render(res, 'appsearch.html', {})
