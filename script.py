from Payroll.apps.employee.models import Payroll,Employee
import pandas as pd

df=pd.read_csv('payrollCSV.csv')
dates=[date for date in df['date'].dropna()]
# employee={"official_email" :[],"incentive": []}
# for email,incentive in zip (df['email'],df['incentive']):
#     employee['official_email'].append(email)
#     employee['incentive'].append(incentive)

for date in dates:
    for email,incentive in zip (df['email'],df['incentive'].fillna(0)):
        Payroll.objects.create(employee=Employee.objects.get(pk=email),monthly_incentive=incentive,salary_issued_date=date)

        
