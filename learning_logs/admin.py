from django.contrib import admin
from learning_logs.models import Topic, Entry  # or .models for current app

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)