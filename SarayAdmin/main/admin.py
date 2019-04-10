from datetime import datetime
from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', )

    def get_exclude(self, request, obj=None):
        exclude = ()
        
        if obj:
            exclude = ('groups', 'user_permissions', )
            if request.user == obj:
                exclude += ()
            else:
                exclude += ('password', )

        return exclude

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ()

        if obj:
            readonly_fields += ('last_login', )
            if request.user == obj:
                readonly_fields += ('is_active', 'is_staff', 'is_superuser', )
            elif request.user.is_superuser:
                readonly_fields += ('username', 'firstname', 'lastname', 'email', 'is_staff', 'is_superuser', )

        return readonly_fields