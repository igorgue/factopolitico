import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse

from facto.models import Country, Fact, Person, Category

def home(request):
    # Summaries
    n = 4
    facts_n = 3

    countries = Country.objects.all()
    people = Person.objects.all()
    recent_facts = Fact.recent_facts(facts_n)
    categories = Category.objects.all()[:n]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def get_country(request, slug):
    country = get_object_or_404(Country, slug=slug)
    return render_to_response('get_country.html', locals(), context_instance=RequestContext(request))

def country_fact_list(request, slug):
    country = get_object_or_404(Country, slug=slug)
    facts_list = country.facts_by_country()
    paginator = Paginator(facts_list, 25)

    page = request.GET.get('page')

    try:
        facts = paginator.page(page)
    except PageNotAnInteger:
        facts = paginator.page(1)
    except EmptyPage:
        facts = paginator.page(paginator.num_pages)

    return render_to_response('country_facts.html', locals(), context_instance=RequestContext(request))

def people(request):
    people_list = Person.objects.all()
    paginator = Paginator(people_list, 25)

    page = request.GET.get('page')

    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    return render_to_response('people.html', locals(), context_instance=RequestContext(request))

def get_people(request, slug):
    person = get_object_or_404(Person, slug=slug)
    more_facts_list = person.more_facts_in_profile()

    paginator = Paginator(more_facts_list, 3)

    page = request.GET.get('page')

    try:
        more_facts = paginator.page(page)
    except PageNotAnInteger:
        more_facts = paginator.page(1)
    except EmptyPage:
        more_facts = paginator.page(paginator.num_pages)

    return render_to_response('get_people.html', locals(), context_instance=RequestContext(request))

def get_fact(request, people_slug, fact_slug):
    fact = get_object_or_404(Fact, slug=fact_slug, person__slug=people_slug)
    return render_to_response('get_fact.html', locals(), context_instance=RequestContext(request))

def recent_facts(request):
    recent_facts_by_date = Fact.recent_facts()
    return render_to_response('recent_facts.html', locals(), context_instance=RequestContext(request))

def get_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    facts_list = category.facts()

    paginator = Paginator(facts_list, 3)

    page = request.GET.get('page')

    try:
        facts = paginator.page(page)
    except PageNotAnInteger:
        facts = paginator.page(1)
    except EmptyPage:
        facts = paginator.page(paginator.num_pages)
    return render_to_response('get_category.html', locals(), context_instance=RequestContext(request))

def save_bm_fact(request):
    p_id = request.GET['person']
    c_id = request.GET['category']
    # if not p_id or not c_id:
    person = get_object_or_404(Person, id=p_id)
    category = get_object_or_404(Category, id=c_id)
    response_data = {}
    f = Fact.objects.create(title='BMADD', quote=request.GET['quote'], person=person, category=category)
    # try:
        
    #     # url=
    # except:
    #     response_data['status'] = 'error'
    # else:
    response_data['status'] = 'ok'
    return HttpResponse("%s(%s)" % (request.GET['callback'], json.dumps(response_data)), content_type="application/json")

def show_bookmarklet(request):
    people = Person.objects.all()
    catz = Category.objects.all()
    return render_to_response('bm.js', locals(), context_instance=RequestContext(request))