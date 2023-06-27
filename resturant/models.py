from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guests = models.IntegerField(default= 2, null= False,
                                       validators=[
                                           MaxValueValidator(6),
                                           MinValueValidator(1)
                                                    ]
                                       )
    booking_date = models.DateField(default=datetime.now, null=False)
    
    def __str__(self):
        return f"{self.name}, {self.booking_date}"

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    inventory = models.IntegerField(default=5)
    
    def __str__(self):
        return f"{self.title}, {self.price}$"    