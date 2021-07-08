from django.contrib import admin

# Register your models here.
from .models import User, medicine, manufacture, patient, buy, bill

admin.site.register(User)
admin.site.register(medicine)
admin.site.register(manufacture)
admin.site.register(patient)
admin.site.register(buy)
admin.site.register(bill)