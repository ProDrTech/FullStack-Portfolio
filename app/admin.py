from django.contrib import admin
from .models import *
# Register your models here.

class HeroCaruselInlene(admin.TabularInline):
    model = HeroCarusel

class HeroImageInlene(admin.TabularInline):
    model = HeroImage

class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'direction')
    inlines = [HeroCaruselInlene, HeroImageInlene]

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number')

class ServiceHighlightInlene(admin.TabularInline):
    model = ServiceHighlight

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc', 'image')
    inlines = [ServiceHighlightInlene]

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroCarusel)
admin.site.register(HeroImage)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceHighlight)