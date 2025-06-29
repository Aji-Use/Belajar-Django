from django.contrib import admin
from .models import Appuser, Administrator

# Register your models here.
admin.site.register(Appuser)
admin.site.register(Administrator)