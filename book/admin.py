from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant, Reservation

@admin.register(Reservation)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('restaurant', 'reservation_date', 'reservation_time', 'party_size', 'user', 'requirements', 'status')
    search_fields = ['reservation_date', 'reservation_time', 'user', 'requirements', 'status']
    list_filter = ('reservation_date', 'reservation_time', 'user', 'status')
    summernote_fields = ('requirements',)

# Register your models here.
admin.site.register(Restaurant)
