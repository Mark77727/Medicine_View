"""import modules"""


import django_filters


"""import models"""

from.models import Purchase


"""filters Purchase"""


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = ['hospital_name',
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
                  ]



