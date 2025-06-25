from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.utilisateur)
admin.site.register(models.Note)

