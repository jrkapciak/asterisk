from django.contrib import admin


class TimeStampedUUIDAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "uuid")
