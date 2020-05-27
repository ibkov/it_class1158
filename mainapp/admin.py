from django.contrib import admin
from .models import Puples, Events, Works, DaysTask, ApplicantAction


class EventsAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "events")
    list_display_links = ("name",)
    list_filter = ("date", "name", "events__surname")
    search_fields = ("name", "events__surname", "events__name")


class WorksAdmin(admin.ModelAdmin):
    list_display = ("date", "name")
    list_filter = ("date", "name")
    list_display_links = ("name",)

class ApplicantActionAdmin(admin.ModelAdmin):
    list_display = ("action_app", "check","date")
    search_fields = ("action_app__name", "action_app__surname")
    list_filter = ("action_app__surname", "date")

admin.site.register(Puples)
admin.site.register(Events, EventsAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(DaysTask)
admin.site.register(ApplicantAction, ApplicantActionAdmin)

# Register your models here.
