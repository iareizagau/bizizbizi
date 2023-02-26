from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("id", "log_count", "user", "mountain_club", "public", "created", "updated")
    search_fields = ("user", "mountain_club", "public", "created", "updated")
    list_filter = ("user", "mountain_club", "public", "created", "updated")
    # list_editable = ("user", "enable", "town",)
    ordering = ("-log_count",)


admin.site.register(Profile, ProfileAdmin)
