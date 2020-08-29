from django.contrib import admin
from webapp.models import Poll, Choice
# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)