from django.db import models

# Create your models here.
class Investor(models.Model):
    email =  models.CharField(max_length=100 ,   default='SOME STRING')
    name =  models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=15)
    risk_tolerance = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')] ,   default ='low')
    investment_horizon = models.IntegerField(max_length=100 ,default=0  )  # in years
    initial_investment = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    income = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    financial_goals = models.TextField(default='SOME STRING')


    class Meta : 
        db_table = 'investor'
    def __str__(self):
        return f"Employee(Name: {self.name})"

