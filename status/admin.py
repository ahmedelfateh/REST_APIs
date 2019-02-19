from django.contrib import admin

from .forms import StatusForm

from .models import Status

# Register your models here.


class StatusAdmin(admin.ModelAdmin):

    form = StatusForm


admin.site.register(Status, StatusAdmin)
