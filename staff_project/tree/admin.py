from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from tree.models import Subdivisions, Staff

admin.site.register(Staff, admin.ModelAdmin)
admin.site.register(Subdivisions, MPTTModelAdmin)
