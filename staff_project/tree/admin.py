from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from tree.models import Subdivisions, Staff


# class StaffAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


admin.site.register(Staff, admin.ModelAdmin)


# class SubdivisionsAdmin(MPTTModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


admin.site.register(Subdivisions, MPTTModelAdmin)

