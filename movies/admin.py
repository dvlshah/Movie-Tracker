from django.contrib import admin
from .models import Movies,Actor,Director
# Register your models here.
admin.site.register(Movies)
admin.site.register(Actor)
admin.site.register(Director)
