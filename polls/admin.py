from django.contrib import admin
from .models import poll,Choice,Vote
# Register your models here.
admin.site.register(poll)
admin.site.register(Choice)
admin.site.register(Vote)

