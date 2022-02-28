from django.contrib import admin

from . import models


class PersonAdmin(admin.ModelAdmin):
	list_display = ('mastery_class', 'author')


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Mastery)
admin.site.register(models.MasterClass)