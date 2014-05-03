from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def countries(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

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
