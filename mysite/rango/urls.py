import about as about
from django.conf.urls import url, include
from rango import views
from rango import viewsAbout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/', viewsAbout.about, name='about'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)