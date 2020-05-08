from django.contrib import admin

from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "name", "address", "email")
    search_fields = ("username", "name", "address", "phone", "email")


class truckAdmin(admin.ModelAdmin):
    list_display = ("title", "sump",)
    search_fields = ("title",)
    list_filter = ("title",)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ("truck", "num", "com", "fen")
    search_fields = ("truck", "num", "com", "fen")


class ActionAdmin(admin.ModelAdmin):
    def show_all_join(self, obj):
        return [a.name for a in obj.user.all()]

    def num(self, obj):
        return obj.user.count()

    list_display = ("title", "num", "status")
    search_fields = ("title", "content", "user")
    list_filter = ("status",)


class CommenAdmin(admin.ModelAdmin):
    list_display = ("user", "truck", "good", "create_time")
    search_fields = ("user", "truck", "good")
    list_filter = ("user", "truck")


class ActionCommenAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "create_time")
    search_fields = ("user", "action")
    list_filter = ("user", "action")


class LiuyanAdmin(admin.ModelAdmin):
    list_display = ("user", "create_time")
    search_fields = ("user",)
    list_filter = ("user",)


class NumAdmin(admin.ModelAdmin):
    list_display = ("users", "trucks", "comments", "actions", "message_boards")


admin.site.register(Tags)
admin.site.register(User, UserAdmin)
admin.site.register(Truck, truckAdmin)
admin.site.register(Comment, CommenAdmin)
# admin.site.register(Num, NumAdmin)
