from django.db import models


class MilkProduct(models.Model):
    MILK_TYPES = [
        ('milk', 'Milk'),
        ('mala', 'Mala'),
        ('yoghurt', 'Yoghurt'),
    ]
    name = models.CharField(max_length=255)
    price_per_litre = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Product: {self.name} - Price: {self.price_per_litre} - Stock: {self.stock}"


class Soda(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    items = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer_name} at {self.created_at}"
