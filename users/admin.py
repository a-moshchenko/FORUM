from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'get_image', 'is_staff',
                    'is_active',)
    list_filter = ('name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'email', 'avatar', 'password1', 'password2',
                'is_staff', 'is_active'
                )}
         ),
    )
    search_fields = ('email', 'name',)
    ordering = ('email', 'name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60" ')

    get_image.short_description = 'аватар'


admin.site.register(CustomUser, CustomUserAdmin)
