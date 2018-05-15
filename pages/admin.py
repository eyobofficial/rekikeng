from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserModel(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'last_login', ]
    filter_horizontal = ['groups', ]
    exclude = ['user_permissions', ]
    readonly_fields = ['last_login', 'date_joined']

    def full_name(self, obj):
        return obj.get_full_name()


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated_at', ]
    fieldsets = [
        ('Company Details', {
            'fields': (
                'name', 'tagline',
                'location', 'subcity', 'city', 'country',
                'phone', 'email',
            ),
        }),
        ('Company Logo', {
            'fields': ('logo', 'logo_hover', 'logo_mobile', 'fevicon', ),
        }),
        ('About Us', {
            'fields': (
                'quote', 'quote_speaker',
                'description1', 'description2', 'team_description',
            ),
        }),
        ('Social Media Accounts', {
            'fields': (
                'facebook', 'twitter', 'instagram', 'linkedin',
            ),
        }),
    ]


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'updated_at', ]
    search_fields = ['full_name', 'position', 'bio', ]


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]
    search_fields = ['title', 'description', ]


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]
