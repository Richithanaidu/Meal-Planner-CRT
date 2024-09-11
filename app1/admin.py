from django.contrib import admin
from .models import register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'gender', 'desig')  # Display these fields in admin

admin.site.register(register, RegisterAdmin)
