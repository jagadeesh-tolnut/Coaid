from django.db import models
from datetime import datetime

# Create your models here.
class updateinfo(models.Model):
    date = models.DateField()
    timesnap = models.TimeField()
    Continent = models.CharField(max_length=5,default='Asia')
    Country = models.CharField(max_length=6, default='India')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{}--{}'.format(self.Country, self.timesnap)

    def srtime(self):
        return datetime.strftime(self.timesnap, '%h:%m:%s')

class Active_cases(models.Model):
    date = models.DateField()
    active = models.IntegerField()
    critical = models.IntegerField()
    new = models.IntegerField()
    recovered = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)

class Death_cases(models.Model):
    date = models.DateField()
    new = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)

class Covid_tests(models.Model):
    date = models.DateField()
    total = models.IntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)


