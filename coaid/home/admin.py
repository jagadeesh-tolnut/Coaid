from django.contrib import admin
from .models import Active_cases, Death_cases, Covid_tests, updateinfo

# Register your models here.
class Display(admin.ModelAdmin):
    list_display = ('date','total')

class forUpdateInfo(admin.ModelAdmin):
    list_display = ('date', 'timesnap')

admin.site.register(Active_cases, Display)
admin.site.register(Death_cases, Display)
admin.site.register(Covid_tests, Display)
admin.site.register(updateinfo, forUpdateInfo)