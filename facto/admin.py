from django.contrib import admin
from facto.models import Country, Fact, Person, Category

class PersonAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class FactAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Country, CountryAdmin)