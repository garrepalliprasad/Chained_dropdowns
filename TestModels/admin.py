from django.contrib import admin
from .models import District,Mandal,Village
# Register your models here.
admin.site.register([District,Mandal,Village])