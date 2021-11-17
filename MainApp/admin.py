from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.register(Entry)
admin.site.register(Topic)
