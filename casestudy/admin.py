from django.contrib import admin
from .models import CaseStudy, Item

# Register your models here.

class CaseStudyAdmin(admin.ModelAdmin):
    pass

admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(Item)
