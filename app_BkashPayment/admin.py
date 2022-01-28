from django.contrib import admin
from .models import BkashPayment, BkashTransaction
admin.site.register([BkashPayment, BkashTransaction])