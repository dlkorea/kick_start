from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth import get_user_model
from .models import Language, Question, Answer, Profile


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]


admin.site.register(Language)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.unregister(get_user_model()),
admin.site.register(get_user_model(), UserAdmin)
