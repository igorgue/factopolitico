from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'facto.views.home', name='home'),

    url(r'^countries/(?P<slug>[\w-]+)/$', 'facto.views.get_country', name='get_country'),
    url(r'^countries/(?P<slug>[\w-]+)/facts/$', 'facto.views.country_fact_list', name='country_fact_list'),

    url(r'^people/(?P<slug>[\w-]+)/$', 'facto.views.get_people', name='get_people'),
    url(r'^people/(?P<people_slug>[\w-]+)/facts/(?P<fact_slug>[\w-]+)/$', 'facto.views.get_fact', name='get_fact'),

    url(r'^recent_facts/$', 'facto.views.recent_facts', name='recent_facts'),

    url(r'^categories/(?P<slug>[\w-]+)/$', 'facto.views.get_category', name='get_category'),

    url(r'^bm.js$', 'facto.views.show_bookmarklet', name='show_bookmarklet'),
    url(r'^facts/save/$', 'facto.views.save_bm_fact', name='save_bm_fact'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
