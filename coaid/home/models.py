from django.db import models

# Create your models here.
class Active_cases(models.Model):
    date = models.DateField()
    cases = models.IntegerField()

    def __str__(self):
        return self.date

class Death_cases(models.Model):
    date = models.DateField()
    cases = models.IntegerField()

    def __str__(self):
        return self.date

