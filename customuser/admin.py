from django.contrib import admin
from .models import CustomUser


# Register your models here.
# admin.site.register(CustomUser)
@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'gender', 'dob', 'is_staff')
    fieldsets = [(None, {'fields': ['firstname', 'lastname', 'email', 'gender', 'dob',
                                    'contact', 'is_staff', 'is_active']}), ]
    list_filter = ('gender', 'is_active')
    search_fields = ('firstname',)
