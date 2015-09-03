from django.contrib import admin
from application.models import Member
from application.models import Event

admin.site.register(Member)
admin.site.register(Event)