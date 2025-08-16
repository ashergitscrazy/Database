from django.contrib import admin
from .models import Client, Course, SignIn, SheetImport
from .utils import import_sheet


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    ordering = ("last",)
    list_display = ("last", "first")
    search_fields = ("last__startswith",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ("name", "instructor")
    search_fields = ("name__contains",)


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ("client", "course", "signintime")

    def signintime(self, obj):
        return obj.timestamp

    signintime.short_description = "Sign In Day / Time"

    ordering = ("-timestamp",)


@admin.register(SheetImport)
class SheetImportAdmin(admin.ModelAdmin):
    list_display = ("sheet_url",)
    actions = ["import_data"]

    def import_data(self, request, queryset):
        for sheet in queryset:
            import_sheet(sheet.sheet_url)
        self.message_user(request, "Sheet imported successfully!")

    import_data.short_description = "Import data from selected Sheets"
