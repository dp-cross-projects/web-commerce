from django.contrib import admin
from .models import UserData, UserHistory

# Register your models here.
admin.site.register(UserData)
admin.site.register(UserHistory)