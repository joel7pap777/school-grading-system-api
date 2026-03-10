from django.contrib import admin
from .models import Result


class ResultAdmin(admin.ModelAdmin):
    readonly_fields = ('total', 'grade')


admin.site.register(Result, ResultAdmin)