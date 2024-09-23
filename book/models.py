from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Cancelled"))

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant_images', null=True, blank=True)
    tables = models.IntegerField(max_length=20)
    capacity = models.IntegerField(default=80)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    party_size = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
