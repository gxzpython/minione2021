from django.contrib import admin

# Register your models here.
from society.models import Group, Event, People,NewUser

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(People)
admin.site.register(NewUser)