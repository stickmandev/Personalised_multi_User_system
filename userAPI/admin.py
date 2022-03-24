from django.contrib import admin

from .models import CustomUser
from .models import jwt

# Register your models here.

admin.site.register(jwt)
admin.site.register(CustomUser)
