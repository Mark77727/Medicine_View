"""import modules"""

from django.shortcuts import render
from .filters import PurchaseFilter


"""import models"""

from.models import Purchase


"""render templates"""


def index(request):
    hospital = Purchase.objects.all()
    purchase_filter = PurchaseFilter(request.GET, queryset=hospital)
    hospital = purchase_filter.qs
    return render(request, 'registry/html/index.html',
                  {
                      'hospital': hospital,
                      'purchase_filter': purchase_filter,
                  }
                  )
