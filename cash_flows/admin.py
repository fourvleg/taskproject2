from django.contrib import admin
from .models import *


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    list_filter = (
        ("date", admin.DateFieldListFilter),
        "status",
        "type",
        "category",
        "subcategory",
    )
    search_fields = ("comment",)

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}


admin.site.register([Status, SubCategory, Type, Category])
