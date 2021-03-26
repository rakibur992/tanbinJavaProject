from django.db import models
from django.db.models import fields
from django import forms
from .models import Payroll
from bootstrap_datepicker_plus import DatePickerInput

class PayrollGenerator (forms.ModelForm):
    class Meta :
        model = Payroll
        fields = ("employee","salary_issued_date")
        widgets = {
            "employee": forms.Select(attrs={'class': 'form-control'}),
            'salary_issued_date': DatePickerInput(format='%m/%d/%Y')   
        }

