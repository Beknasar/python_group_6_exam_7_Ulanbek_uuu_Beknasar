from django.contrib import admin
from webapp.models import Poll, Choice, Answer

# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)