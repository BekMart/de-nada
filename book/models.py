from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"), (3, "Cancelled"))

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    capacity = models.IntegerField(default=80)
    tables = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.name}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    party_size = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    requirements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["reservation_date", "reservation_time"]

    def __str__(self):
        return f"{self.restaurant} | {self.reservation_date} | {self.reservation_time} | {self.user} | ({self.party_size})"