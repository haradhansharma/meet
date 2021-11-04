from django.contrib import admin
from django.contrib.admin.decorators import display

from . models import Meetup, Location, Participant

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)
    list_filter = ('location', )
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'location']

    

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)


