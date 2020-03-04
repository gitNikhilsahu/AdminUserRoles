from django.contrib import admin

from Accounts import models


admin.site.register(models.User)
admin.site.register(models.ProfileStatus)
