from django.db import models
from datetime import datetime

# Create your models here.

class Search_by_pin(models.Model):
    date = models.DateField(auto_now=datetime.now())
    pincode = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return '{}--{}'.format(self.pincode, self.date)

