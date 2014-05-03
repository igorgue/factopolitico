from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, blank=False)
    #picture = models.ImageField(upload_to='public/images/upload', height_field=80, width_field=80)#, max_length=100)
    picture_url = models.URLField(max_length=200, blank=True)

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def facts_by_country(self):
        return Fact.objects.filter(person__country=self)

    def persons(self):
        return People.objects.filter(country=self)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    #profile_pic = models.ImageField(upload_to='public/images/upload', height_field=80, width_field=80)#, max_length=100)
    profile_pic_url = models.URLField(max_length=200, blank=True)

    country = models.ForeignKey(Country, related_name='country')

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255, blank=False)

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def facts_count(self):
        return Fact.objects.filter(category=self).count()

    def __unicode__(self):
        return self.title

class Fact(models.Model):
    STATUS = (
        ('investigating', 'Investigando'),
        ('almost-true', 'Casi Vedad'),
        ('true', 'Verdad'),
        ('half-true', 'Media Verdad'),
        ('false', 'Falso'),
        ('mostly-false', 'Sobretodo Falso'),
        ('pants-on-fire', 'Tremenda Mentira!'),
    )

    title = models.CharField(max_length=255, blank=False)
    quote = models.TextField(blank=False)
    video = models.TextField(blank=True) # embed code
    content = models.TextField(blank=False)
    status = models.CharField(max_length=255, choices=STATUS, blank=True, default=STATUS[0][0])
    # ^^^ get_status_display to show name in templates

    user = models.ForeignKey(User, blank=True, null=True)
    person = models.ForeignKey(Person, related_name='person')
    category = models.ForeignKey(Category, related_name='category')

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def __unicode__(self):
        return self.title

    @classmethod
    def recent_facts(cls, number=5):
        return cls.objects.all().order_by('-created_at')[:number]

class Source(models.Model):
    url = models.URLField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)

    fact = models.ForeignKey(Fact, related_name='fact')

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def __unicode__(self):
        return self.title
