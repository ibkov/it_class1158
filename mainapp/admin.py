from django.contrib import admin
from .models import Puples, Events, Works, DaysTask


class EventsAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "events")
    list_display_links = ("name",)
    list_filter = ("date", "name", "events__surname")
    search_fields = ("name", "events__surname", "events__name")


class WorksAdmin(admin.ModelAdmin):
    list_display = ("date", "name")
    list_filter = ("date", "name")
    list_display_links = ("name",)


admin.site.register(Puples)
admin.site.register(Events, EventsAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(DaysTask)

# Register your models here.
