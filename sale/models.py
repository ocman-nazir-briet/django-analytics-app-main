from email.policy import default
from uuid import uuid4
from xmlrpc.client import Boolean
from django.db import models
from django.forms import BooleanField
from pytz import timezone
from profiles.models import *
from products.models import *
from shop.models import *
from .utils import generate_code
from django.shortcuts import reverse

class Position(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id
        
    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}, price: {self.price}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=16, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(myUser, on_delete=models.CASCADE)
    saleman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale for the amount of: ${self.total_price}"
    
    def save(self, *args, **kwargs):
        if self.transaction_id == "":                                      # self.transaction_id = str(uuid.uuid4()).replace('-', '').upper()[:12]
            self.transaction_id = generate_code()                          # instead of utils we can use above line too
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse('sale:DetailView', kwargs={'pk': self.pk})
    

class CSV(models.Model):
    file_name = models.FileField(upload_to="CSVS")
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.filename)