from django.db import models

# Create your models here.


class myUser(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='userPics', default='noPic.png')

    
    def __str__(self):
        return str(self.name)
