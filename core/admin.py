"""
Django admin customization.
"""

from django.contrib import admin  # type: ignore
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # type: ignore
from django.utils.translation import gettext_lazy as _  # pyright: ignore[reportMissingModuleSource]

from core.models import (
    Alternativa,
    Cronograma,
    CronogramaItem,
    Exercicio,
    Materia,
    User,
)


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']

    list_display = [
        'email',
        'name',
    ]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {
                'fields': (
                    'name',
                    'foto',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (
            _('Important dates'),
            {'fields': ('last_login',)},
        ),
        (
            _('Groups'),
            {'fields': ('groups',)},
        ),
        (
            _('User Permissions'),
            {'fields': ('user_permissions',)},
        ),
    )

    readonly_fields = ['last_login']

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'foto',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Materia)
admin.site.register(Exercicio)
admin.site.register(Alternativa)
admin.site.register(Cronograma)
admin.site.register(CronogramaItem)
