from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserModel(admin.ModelAdmin):
    list_display = ['username', ]
    filter_horizontal = ['groups', ]


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', ]
    search_fields = ['full_name', 'position', 'bio', ]


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', 'description', ]


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', ]
