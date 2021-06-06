from django.urls import path, include
from .views import *
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name='keyword_finder_main'),
    path('get_keywords', get_keywords, name='get_keywords'),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]+ static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)
