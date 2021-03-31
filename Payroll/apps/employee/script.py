from Payroll.apps.employee.models import Payroll,Employee,SalaryPackage,FinancialYear
import pandas as pd
from datetime import datetime
df=pd.read_csv('payrollCSV.csv')
dates=[date for date in df['date'].dropna()]
# employee={"official_email" :[],"incentive": []}
# for email,incentive in zip (df['email'],df['incentive']):
#     employee['official_email'].append(email)
#     employee['incentive'].append(incentive)

for date in dates:
    for email,incentive in zip (df['email'],df['incentive'].fillna(0)):
        payroll=Payroll.objects.create(employee=Employee.objects.get(pk=email),monthly_incentive=incentive,salary_issued_date=datetime.strptime(date,"%m/%d/%Y").date())
    payroll.save()

# Reset salary Package
for email,incentive in zip (df['email'],df['incentive'].fillna(0)):
    sp=SalaryPackage.objects.filter(employee=email).order_by('-id').first()
    print(sp)
    sp.monthly_incentive=0
    sp.special_allowence_7=0
    # sp.tax_paid_this_year_without_investment=0
    # sp.tax_paid_this_year_with_rebate=0
    sp.save()

prev_payroll = Payroll.objects.all().filter(employee=Employee.objects.get(pk="rahamatullah@fashionlinq.com"),financial_year=FinancialYear.objects.get(current_year=True).financial_year_end) 
sum([x.tax_this_month_without_investment for x in prev_payroll])
sum([x.tax_this_month_with_rebate for x in prev_payroll])