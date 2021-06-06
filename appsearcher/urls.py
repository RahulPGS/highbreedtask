from django.urls import path, include
from .views import *
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name='appsearcher_main'),
    path('search_app_store/<str:name>/<int:id>', search_app, name='search_app_store'),
    path('search_play_store/<str:name>', search_app, name='search_play_store'),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]+ static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)
