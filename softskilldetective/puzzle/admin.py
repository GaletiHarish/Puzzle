from django.contrib import admin
from .models import User, Clue, UserProgress

admin.site.register(User)
admin.site.register(Clue)
admin.site.register(UserProgress)
