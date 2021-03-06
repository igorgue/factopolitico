import random

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    profile_pic_url = models.URLField(max_length=255, blank=True)
    blur = models.TextField(blank=True)

class Country(models.Model):
    name = models.CharField(max_length=255, blank=False)
    #picture = models.ImageField(upload_to='public/images/upload', height_field=80, width_field=80)#, max_length=100)
    picture_url = models.URLField(max_length=255, blank=True)

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def latest_fact(self):
        facts = Fact.objects.filter(person__country=self).order_by('-created_at')

        if facts.count() > 0:
            return facts[0]
        else:
            return None

    def facts_by_country(self):
        return Fact.objects.filter(person__country=self)

    def facts_count(self):
        return self.facts_by_country().count()

    def people(self):
        return Person.objects.filter(country=self)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)

        super(Country, self).save(*args, **kwargs)

class Person(models.Model):
    name = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    #profile_pic = models.ImageField(upload_to='public/images/upload', height_field=80, width_field=80)#, max_length=100)
    profile_pic_url = models.URLField(max_length=255, blank=True)

    country = models.ForeignKey(Country, related_name='country')

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def more_facts_in_profile(self):
        return Fact.objects.filter(person=self).order_by('-created_at')[1:]

    def latest_fact(self):
        facts = Fact.objects.filter(person=self).order_by('-created_at')
        if facts.count() > 0:
            return facts[0]
        else:
            return None

    def facts(self):
        return Fact.objects.filter(person=self)

    def facts_breakdown(self):
        investigating = Fact.objects.filter(person=self, status=Fact.STATUS[0][0]).count()
        almost_true = Fact.objects.filter(person=self, status=Fact.STATUS[1][0]).count()
        true = Fact.objects.filter(person=self, status=Fact.STATUS[2][0]).count()
        half_true = Fact.objects.filter(person=self, status=Fact.STATUS[3][0]).count()
        false = Fact.objects.filter(person=self, status=Fact.STATUS[4][0]).count()
        mostly_false = Fact.objects.filter(person=self, status=Fact.STATUS[5][0]).count()

        breakdown = {
            'investigating': "{:.0%}".format(float(investigating) / float(self.facts_count())),
            'almost_true': "{:.0%}".format(float(almost_true) / float(self.facts_count())),
            'true': "{:.0%}".format(float(true) / float(self.facts_count())),
            'half_true': "{:.0%}".format(float(half_true) / float(self.facts_count())),
            'false': "{:.0%}".format(float(false) / float(self.facts_count())),
            'mostly_false': "{:.0%}".format(float(mostly_false) / float(self.facts_count()))
        }

        return breakdown

    def facts_count(self):
        return self.facts().count()

    def categories(self):
        return Category.objects.filter(id__in=list(set([fact.category.id for fact in self.facts()])))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)

        super(Person, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=255, blank=False)

    slug = models.SlugField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def facts(self):
        return Fact.objects.filter(category=self)

    def facts_count(self):
        return self.facts().count()

    def facts_count_by_person(self, person):
        return Fact.objects.filter(category=self, person=person).count()

    def countries(self):
        return Country.objects.filter(id__in=list(set([fact.person.country.id for fact in self.facts()])))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

class Fact(models.Model):
    STATUS = (
        ('investigating', 'Investigando'),
        ('almost-true', 'Casi Verdad'),
        ('true', 'Verdad'),
        ('half-true', 'Media Verdad'),
        ('mostly-false', 'Medio Falso'),
        ('false', 'Falso!'),
    )

    title = models.CharField(max_length=255, blank=False)
    quote = models.TextField(blank=False)
    image_url = models.URLField(max_length=255, blank=True)
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

    def status_css_class(self):
        if self.status == 'investigating':
            return 'default'
        elif self.status == 'false':
            return 'danger'
        elif self.status == 'mostly-false':
            return 'danger'
        elif self.status == 'half-true':
            return 'primary'
        elif self.status == 'almost-true':
            return 'info'
        elif self.status == 'true':
            return 'success'

    def country_image_url(self):
        return self.person.country.picture_url

    def __unicode__(self):
        return self.title

    def sources(self):
        return Source.objects.filter(fact=self)

    def save(self, *args, **kwargs):
        if self.slug == '':
            x = random.randint(1, 99999999999)
            self.slug = slugify(u"%s" % self.title+' '+str(x))

        super(Fact, self).save(*args, **kwargs)

    @classmethod
    def recent_facts(cls, number=5):
        return cls.objects.all().order_by('-created_at')[:number]

class Source(models.Model):
    url = models.URLField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=True)

    fact = models.ForeignKey(Fact, related_name='fact')
    content = models.TextField(blank=True)

    slug = models.SlugField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, blank=False, null=False)

    def __unicode__(self):
        return self.title
