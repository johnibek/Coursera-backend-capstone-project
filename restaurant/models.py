from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.title

    def get_item(self):
        return f"{self.title} : {self.price}"

