from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booktable(request):
    return HttpResponse("BOOK A TABLLE HERE!")

# def make_reservation(request):
#     # ... other form validation and processing

#     # Check table availability
#     table_availability = TableAvailability.objects.filter(
#         table=selected_table,
#         reservation_date=reservation_date,
#         reservation_time=reservation_time
#     ).first()

#     if not table_availability or not table_availability.is_available:
#         # Redirect back to booking form with error message
#         messages.error(request, 'The table is not available for that time.')
#         return render(request, 'booking_form.html', {'form': form})

#     # ... create reservation and update table availability