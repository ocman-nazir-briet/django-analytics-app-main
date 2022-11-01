from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='ProductsPics', default='noPic.png')
    price = models.FloatField(help_text='in US $')
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%y')}"