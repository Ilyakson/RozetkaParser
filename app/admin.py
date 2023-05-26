from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from .models import Keyword, Link, Info


def link(obj):
    return format_html("<a href='{url}''>{url}</a>", url=obj.site)


@admin.register(Keyword)
class SkypeChatAdmin(ModelAdmin):
    list_display = ["name", "status"]
    fields = ["name", "status"]


@admin.register(Link)
class SettingAdmin(ModelAdmin):
    list_display = ["name", "link", "status"]


@admin.register(Info)
class TelegramBotAdmin(ModelAdmin):
    list_display = ["product_name", "price", "link", "reviews"]
    fields = [
        "product_name", "price",
        "link", "reviews",
        "screen_diagonal", "sim_card_count",
        "built_in_memory", "front_camera", "main_camera"
    ]
