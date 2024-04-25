from django.contrib import admin
from .models import Client, Course, SignIn


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    ordering = ("last", )
    list_display = ("last", "first")
    search_fields = ("last__startswith",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ("name", )
    list_display = ("name", "instructor")
    search_fields = ("name__contains",)


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ("client", "course", "signintime")

    def signintime(self, obj):
        return obj.timestamp

    signintime.short_description = "Sign In Day / Time"

    ordering = ("-timestamp", )
