from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from facto.models import Country, Fact, Person, Category

def home(request):
    # Summaries
    n = 4

    countries = Country.objects.all()[:n]
    people = Person.objects.all()[:n]
    recent_facts = Fact.recent_facts(n)
    categories = Category.objects.all()[:n]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def countries(request):
    countries_list = Country.objects.all()
    paginator = Paginator(countries_list, 25)

    page = request.GET.get('page')

    try:
        countries = paginator.page(page)
    except PageNotAnInteger:
        countries = paginator.page(1)
    except EmptyPage:
        countries = paginator.page(paginator.num_pages)

    return render_to_response('countries.html', locals(), context_instance=RequestContext(request))

def get_country(request, slug):
    # country = get_object_or_404(Country, slug=slug)
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
    return render_to_response('get_people.html', locals(), context_instance=RequestContext(request))

def get_fact(request, people_slug, fact_slug):
    fact = get_object_or_404(Fact, slug=fact_slug, person__slug=people_slug)
    return render_to_response('get_fact.html', locals(), context_instance=RequestContext(request))

def recent_facts(request):
    recent_facts_by_date = Fact.recent_facts()
    return render_to_response('recent_facts.html', locals(), context_instance=RequestContext(request))

def categories(request):
    categories = Category.all()
    return render_to_response('categories.html', locals(), context_instance=RequestContext(request))

def get_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('get_category.html', locals(), context_instance=RequestContext(request))

