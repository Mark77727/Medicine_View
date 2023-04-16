from django.contrib import admin


"""import library """


from import_export.admin import ImportExportModelAdmin


"""import models"""


from.models import Purchase


"""register models"""


class PurchaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Purchase, PurchaseAdmin)
