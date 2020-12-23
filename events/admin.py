from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import (
    EventCategory,
    Event,
    EventMember,

)

admin.site.register(EventCategory)
admin.site.register(Event, MapAdmin)
admin.site.register(EventMember)

