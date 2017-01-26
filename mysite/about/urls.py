from django.conf.urls import url, include
from about import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.about, name='about'),
       ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)