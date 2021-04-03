from django.contrib import admin

from aeroplane.models import Page


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
