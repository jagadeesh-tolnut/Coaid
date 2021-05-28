from django.contrib import admin
from .models import Active_cases, Death_cases, Covid_tests, updateinfo

# Register your models here.
admin.site.register(Active_cases)
admin.site.register(Death_cases)
admin.site.register(Covid_tests)
admin.site.register(updateinfo)