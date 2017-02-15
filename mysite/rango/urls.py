import about as about
from django.conf.urls import url, include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^about/', about.about, name='about'),
                  url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
                      views.show_category, name='show_category'),
                  url(r'^category/(?P<category_name_url>\w+)/show_pages/', views.show_pages, name='show_pages'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
