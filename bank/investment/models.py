from django.db import models

# Create your models here.
class Investor(models.Model):
    name =  models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=15)

    class Meta : 
        db_table = 'investor'
    def __str__(self):
        return f"Employee(Name: {self.name})"

