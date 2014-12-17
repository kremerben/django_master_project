from django.contrib import admin

# Register your models here.
from app_name.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff',)
    list_filter = ('first_name', 'last_name', 'username', 'email', 'is_staff',)


admin.site.register(User, UserAdmin)


