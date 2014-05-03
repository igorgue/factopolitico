from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#Home page
	#- Countries
	#- People
	#- Most Recent Facts
	#- Categories

#Country Page
	#- Video background of current event
	#- People
	#- Most recent fact
	#- List of facts / paginated

#Person Page
	#- Name
	#- Title
	#- Truth o meter
	#- Picture
	#- Country
	#- Most active categories

#Fact page
	#- Person
	#- Quote
	#- Truth
	#- Assessment
	#- Sources

urlpatterns = patterns('',
    url(r'^$', 'facto.views.home', name='home'),

    url(r'^countries/$', 'facto.views.countries', name='countries'),
    url(r'^countries/(?P<slug>\w+)/$', 'facto.views.get_country', name='get_country'),
    url(r'^countries/(?P<slug>\w+)/facts/$', 'facto.views.country_fact_list', name='country_fact_list'),

    url(r'^people/$', 'facto.views.people', name='people'),
    url(r'^people/(?P<slug>\w+)/$', 'facto.views.get_people', name='get_people'),
    url(r'^people/(?P<people_slug>\w+)/facts/(?P<fact_slug>\w+)/$', 'facto.views.get_fact', name='get_fact'),

    url(r'^recent_facts/$', 'facto.views.recent_facts', name='recent_facts'),

    url(r'^categories/$', 'facto.views.categories', name='categories'),
    url(r'^categories/(?P<slug>\w+)/$', 'facto.views.get_category', name='get_category'),

    url(r'^admin/', include(admin.site.urls)),
)
