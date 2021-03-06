import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "factopolitico.settings")

import csv

from django.contrib.auth.models import User
from facto.models import *

user = User.objects.get(id=1)

f = open('/Users/igor/Downloads/factos.csv', 'rb')
Fact.objects.all().delete()

reader = csv.reader(f)
next(reader) # skip header
for row in reader:
    fact = Fact()
    fact.person = Person.objects.get(slug=row[1])
    fact.title = row[2].decode('utf-8')
    fact.quote = row[3].decode('utf-8')
    fact.user = user

    category, created = Category.objects.get_or_create(slug=row[11])
    if created or category.title == '':
        category.title = row[11]
        category.save()

    fact.category = category
    fact.status = row[8].lower()
    fact.content = row[9].decode('utf-8')
    fact.image_url = row[12]

    fact.save()

    if row[4] != '':
        try:
            s = Source.objects.get(url=row[4])
        except:
            s = Source()
            s.url = row[4]

        s.fact = fact
        s.url = row[4]
        s.save()

    if row[5] != '':
        try:
            s = Source.objects.get(url=row[5])
        except:
            s = Source()
            s.url = row[5]

        s.fact = fact
        s.url = row[5]
        s.save()

    if row[6] != '':
        try:
            s = Source.objects.get(url=row[6])
        except:
            s = Source()
            s.url = row[6]

        s.fact = fact
        s.url = row[6]
        s.save()

    if row[7] != '':
        try:
            s = Source.objects.get(url=row[7])
        except:
            s = Source()
            s.url = row[7]

        s.fact = fact
        s.url = row[7]
        s.save()
