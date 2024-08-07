from django import forms
from .models import Investor

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = [ 'email','name', 'phone_number' , 'risk_tolerance' , 'investment_horizon', 'initial_investment' , 'income' , 'financial_goals']
