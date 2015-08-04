from django.contrib import admin

# Register your models here.

from django.contrib import admin
from models import *

from admin_enhancer import admin as enhanced_admin

class EnhancedModelAdmin(enhanced_admin.EnhancedModelAdminMixin, admin.ModelAdmin):
    pass

class SpeakerInline(enhanced_admin.EnhancedAdminMixin, admin.StackedInline):
    model = Speaker
    extra = 0

class VideoInline(enhanced_admin.EnhancedAdminMixin, admin.StackedInline):
    model = Video
    extra = 0



class EventAdmin(EnhancedModelAdmin):
#    fieldsets = [
#        (None, {'fields': ['name', 'start_time', 'end_time', 'venue', 'entry_price' ]}),
#        ('Images', {'fields': ['image']}),
#        ('Socials', {'fields': ['meetup', 'facebook', 'eventbrite' ]}),
#        ('Details', {'fields': ['details', 'wrapup' ]}),
#    ]
    list_display = ('name', 'start_time', 'venue')
    inlines = [SpeakerInline, VideoInline]

class ContactInline(admin.StackedInline):
    model = Operator
    extra = 2

class VenueAdmin(EnhancedModelAdmin):
    inlines = [ContactInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Speaker, EnhancedModelAdmin)
admin.site.register(Address, EnhancedModelAdmin)
admin.site.register(Contact, EnhancedModelAdmin)
admin.site.register(Video, EnhancedModelAdmin)


