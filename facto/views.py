from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext

from facto.models import Location

def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def countries(request):
    locations_list = Location.objects.all()
    paginator = Paginator(locations_list, 25)

    page = request.GET.get('page')

    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)

    return render_to_response('countries.html', {'countries': locations}, context_instance=RequestContext(request))

def get_country(request, slug):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def country_fact_list(request, slug):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def people(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def get_people(request, slug):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def get_fact(request, people_slug, fact_slug):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def recent_facts(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def categories(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def get_category(request, slug):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))
