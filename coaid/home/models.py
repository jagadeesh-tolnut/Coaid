from django.db import models

# Create your models here.
class updateinfo(models.Model):
    timesnap = models.CharField(max_length=50)
    Continent = models.CharField(max_length=5,default='Asia')
    Country = models.CharField(max_length=6, default='India')

    def __str__(self):
        return '{}--{}'.format(self.Country, self.timesnap)

class Active_cases(models.Model):
    date = models.DateField()
    active = models.IntegerField()
    critical = models.IntegerField()
    new = models.IntegerField()
    recovered = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.date)

class Death_cases(models.Model):
    date = models.DateField()
    new = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.date)

class Covid_tests(models.Model):
    date = models.DateField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.date)


