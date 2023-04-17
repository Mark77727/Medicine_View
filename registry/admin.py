from django.contrib import admin


"""import library """


from import_export.admin import ImportExportModelAdmin


"""import models"""


from.models import Purchase


"""register models"""


class PurchaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('hospital_name',
                    'name',
                    'cost',
                    'arrive_data',
                    'sent_fin_data',
                    'sent_hospital_data',
                    'sent_correct_data',
                    'comment_text',
                    'p9',
                    'repair',
                    'develop_DED',
                    'PDF_scan',
                    )

    search_fields = ('hospital_name',
                     'name',
                     'cost',
                     'arrive_data',
                     'sent_fin_data',
                     'sent_hospital_data',
                     'sent_correct_data',
                     )


admin.site.register(Purchase, PurchaseAdmin)

