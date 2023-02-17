from django.contrib import admin
from . import models


admin.site.register(models.Food)
admin.site.register(models.Category)
admin.site.register(models.Table)
admin.site.register(models.Event)
admin.site.register(models.BookTable)
