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
