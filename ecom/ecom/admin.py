from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from . import models

from livechat.chat.models import Room, Message
from events.events.models import Venue, Event, MyClubUser

#admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Message)

#admin.site.register(Venue, VenueAdmin)
admin.site.register(MyClubUser)

# Remove Groups
admin.site.unregister(Group)
#admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'event_date', 'description', 'manager')
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('event_date',)

class PostAdmin(admin.ModelAdmin):
	model = models.Post
	list_display = ('excerpt', )

	def excerpt(self, obj):
		return obj.get_excerpt(5)
admin.site.register(models.Post, PostAdmin)

