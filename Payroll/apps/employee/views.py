from Payroll.apps import employee
from django.shortcuts import render
from .models import *
import xlsxwriter
from django.http import HttpResponse, response
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from django.template.context_processors import request
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic import FormView
import csv
import io
from time import  strftime
from io import BytesIO
from django.http import HttpResponse
from Payroll.apps.core.utils.utils import render_to_pdf
from calendar import month, monthrange
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PayrollGenerator
from django.views.decorators.csrf import requires_csrf_token
from django.utils.decorators import method_decorator

# Create your views here.
class MonthlyEmployeePayrollSave(View):
    def post(self,request):
        print(request.Post)
        return response.JsonResponse({"data": "Success"})
class MonthlyEmployeePayroll(LoginRequiredMixin,View):
    template_name = "employee/monthly-payroll.html"
    context_object_name = "data"
    
    def get(self,request,*args,**kwargs):
        object_list={}
        object_list["company"]=self.kwargs.get('company')
        object_list["months"]=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ];
        employee_list = Employee.objects.all().filter(company=self.kwargs.get('company'))
        object_list["employee_data"] = zip([employee for employee in employee_list],[SalaryPackage.objects.get(employee= employee) for employee in employee_list ])
        return render(request,self.template_name,object_list) 
    def post(self,request,*args,**kwargs):
        print(request.POST)
        return response.JsonResponse({"data": "Success"})
    
class GenerateEmployeePayroll(FormView):
    template_name= "employee/payroll-generator.html"
    form_class=PayrollGenerator
    success_url='/employee/Fashionlinq'

    def form_valid(self, form) :
        email=self.kwargs.get('email')
        print(email)
        # Save the validated data of your object
        self.object = form.save(commit = False)
         # Update the value of the desired field
        self.object.employee = Employee.objects.get(pk=email)
         # Save the object to commit the changes
        self.object.save()
        return super().form_valid(form)
    def  get_context_data(self, **kwargs):
        email=self.kwargs.get('email')
        employee= Employee.objects.get(official_email=email)
        context = super().get_context_data(**kwargs)
        context['employee']=employee
        return context     

    # def get_queryset(self,**kwargs):
    #     email=self.kwargs.get('email')
    #     object_list={}
    #     object_list["employee"] = Employee.objects.get(official_email=email)
    #     return object_list
       

class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    template_name = "employee/employee-list.html"
    context_object_name = 'employee_list_data'

    def get_queryset(self,**kwargs):
        object_list={}
        object_list["company"]=self.kwargs.get('company')
        object_list["Employee_list"] = Employee.objects.all().filter(company=self.kwargs.get('company'))
        
        return object_list
  
class EmployeeView(LoginRequiredMixin,DetailView):
    template_name = "employee/employee.html"
    def get(self, request, *args, **kwargs):
        email=request.user.username
        employee = get_object_or_404(Employee, pk=email)
        payroll_data=Payroll.objects.all().filter(employee=email)
        for p in payroll_data:
            print(p.salary_issued_date)
        context = {'employee': employee,
                    'payroll_data':payroll_data}
        
        return render(request, "employee/employee.html", context)


class EmployeeDetailView(LoginRequiredMixin,DetailView):
    models = Employee
    def get(self, request, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=kwargs['pk'])
        payroll_data=Payroll.objects.all().filter(employee=kwargs['pk'])
        
        payroll_id=[]
        for payroll in payroll_data:
            payroll_id.append(employee.official_email+"_"+str(payroll.id))
        context = {'employee': employee,
                    'payroll_data':zip(payroll_data,payroll_id)
                    }
        return render(request, 'employee/employee-detail.html', context)

class AnyEmployExportPayslipToXlxs(View):
    def get(self, request,**kwargs):
        employee_slug=self.kwargs.get('employee_slug')
        email=employee_slug.split('_')[0]
        index=employee_slug.split('_')[1]
        response = getPaySlipRespone(email,index)
        return response
class EmployExportPayslipToXlxs(LoginRequiredMixin,View):

    def get(self, request,**kwargs):
        email=request.user.username
        index=int(self.kwargs.get('index'))
        response = getPaySlipRespone(email,index)
        return response

def getPaySlipRespone (email,index):
             # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Even though the final file will be in memory the module uses temp
        # files during assembly for efficiency. To avoid this on servers that
        # don't allow temp files, for example the Google APP Engine, set the
        # 'in_memory' Workbook() constructor option as shown in the docs.
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        border = workbook.add_format({
            "border":1,
            'align': 'left',
        })
        align_center=workbook.add_format({
            "border":1,
            'align': 'center',
        })
        headborder = workbook.add_format({
            "border":1,
            'align': 'right',
            'fg_color': 'yellow',
            'font_size': 48,
            'font_color':'white'

        })
        worksheet.set_column('A:D',30,border)
        worksheet.set_column('E:E',12,border)

        data=Payroll.objects.get(id=index)
        
        employee_data=Employee.objects.get(official_email=email)
        
        company_data=Company.objects.all().filter(name=employee_data.company)[0]
        company_logo=company_data.company_logo
        
        url="D:\JobProject\payroll\Payroll"+company_logo.url

        worksheet.merge_range('A1:B1','',border)
        worksheet.set_row(0,60)
        worksheet.insert_image(0,0,url,{'x_scale': 0.5, 'y_scale': 0.5})
        worksheet.merge_range('C1:E1','Salary Slip',headborder)

        worksheet.merge_range('A2:E2','Salary For The Month of '+data.salary_issued_date.strftime("%B") +' Year '+data.salary_issued_date.strftime("%Y"),align_center)
        
        #Employee detail
        worksheet.write(2,0,'Name of the Employee')
        worksheet.merge_range('B3:C3',employee_data.name)
        worksheet.write(2,3,'Days in the Month')
        days=monthrange(data.salary_issued_date.year,data.salary_issued_date.month)[1]
        worksheet.write(2,4,days)
        worksheet.write(3,0,'Designation')
        worksheet.merge_range('B4:C4','-')
        worksheet.write(3,3,'Working Days')
        worksheet.write(3,4,'-')

        worksheet.write(4,0,'Department')
        worksheet.write(4,1,'-')
        worksheet.write(4,3,'Date of Joining')
        worksheet.write(4,4,employee_data.joining_date.strftime("%Y-%m-%d"))

        current_row=7
        worksheet.merge_range('A6:E6','')
        worksheet.write(6,0,'Earning')
        worksheet.merge_range('B7:C7','Gross')
        worksheet.merge_range('D7:E7','Deductions')

        earning_attr=company_data.earning_attr.split(',')
        deduction_attr=company_data.deduction_attr.split(',')
        temp_row=0
        for i,earn in enumerate(earning_attr,current_row):
            worksheet.write(i,0,earn)
            m='B'+str(i+1)+':'+'C'+str(i+1)
            value=str(getattr(data,earn))
            worksheet.merge_range(m,value)
            temp_row=i

        for i,deduction in enumerate(deduction_attr,current_row):
            worksheet.write(i,3,deduction)
            value=str(getattr(data,deduction ))
            worksheet.write(i,4,value)
            if i>temp_row:
                temp_row=i

        # Total Earning And Deduction Section        
        current_row=temp_row+1
        worksheet.write(current_row,0,'Total Earning')
        m='B'+str(current_row+1)+':'+'C'+str(current_row+1)
        worksheet.merge_range(m,data.gross_salary_this_month )
        worksheet.write(current_row,3,'Total Deduction')

        # Netpay section 
        current_row+=1
        worksheet.write(current_row,0,'Net Pay')
        m='B'+str(current_row+1)+':'+'E'+str(current_row+1)
        worksheet.merge_range(m,data.net_salary_this_month)

        

        # Close the workbook before sending the data.
        workbook.close()

        # Rewind the buffer.
        output.seek(0)
        
        # Set up the Http response.
        filename = 'PaySlip.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename    
        return response
       

class ExportPayslipToXlxs(View):

    def get(self, request):

        # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Even though the final file will be in memory the module uses temp
        # files during assembly for efficiency. To avoid this on servers that
        # don't allow temp files, for example the Google APP Engine, set the
        # 'in_memory' Workbook() constructor option as shown in the docs.
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        border = workbook.add_format({
            "border":1,
            'align': 'left',
            
        })
        headborder = workbook.add_format({
            "border":1,
            'align': 'right',
            'fg_color': 'yellow',
            'font_size': 48,
            'font_color':'white'

        })
        worksheet.set_column('A:D',30)
        worksheet.set_column('E:E',12)
      
        # Get some data to write to the spreadsheet.
        data =Employee.objects.all()
        row=0
        # Write some test data.
        
        for e in data:
            r1=row+1
            m1='A'+str(r1)+':'+'B'+str(r1)
            r='A'+str(r1)
            worksheet.merge_range(m1,'',border)
            worksheet.set_row(row,60)
            worksheet.insert_image(row,0,'D:\JobProject\payroll\Payroll\Payroll\site_static\site\img\clogo.png',{'x_scale': 0.5, 'y_scale': 0.5})
            m1='C'+str(r1)+':'+'E'+str(r1)
            worksheet.merge_range(m1,'Salary Slip',headborder)
            row+=1
            r1=row+1
            m1='A'+str(r1)+':'+'E'+str(r1)
            b=workbook.add_format({
                "border":1,
                'align': 'center',
                'font_color':'white',
                'bg_color':'#808080',
            })
            worksheet.merge_range(m1,'Salary For The Month of December2020',b)
            row+=1

            worksheet.write(row,0,'Name of the Employee',border)
            worksheet.write(row,1,e.name,border)
            worksheet.write(row,2,'Days in the Month',border)
            worksheet.write(row,3,'-',border)
            row+=1

            worksheet.write(row,0,'Designation',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'Working Days',border)
            worksheet.write(row,3,'-',border)
            row+=1

            worksheet.write(row,0,'Department',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'Date of Joining',border)
            worksheet.write(row,3,e.joining_date,border)
            row+=1

            r1=row+1
            m1='A'+str(r1)+':'+'C'+str(r1)
            worksheet.merge_range(m1,'Earning',border)
            r1=row+1
            m1='D'+str(r1)+':'+'E'+str(r1)
            worksheet.merge_range(m1,'Deductions',border)
            row+=1

            worksheet.write(row,0,'Particulars',border)
            worksheet.write(row,1,'Gross',border)
            worksheet.write(row,2,'Payable',border)
            worksheet.write(row,3,'Provident Fund',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Basic Salary',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,'ESIC',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'House Rent Allowance',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,'Profession Tax',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Conveyance Allowance',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,'Income Tax',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Medical Allowance',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,'Misc. Deduction/ Salary Arrears',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Monthly Incentive',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,' Loan ',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Special Allowance',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            worksheet.write(row,3,'Income Tax',border)
            worksheet.write(row,4,'-',border)
            row+=1
            worksheet.write(row,0,'Salary Arrear',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-',border)
            row+=1
            worksheet.write(row,0,'Total',border)
            worksheet.write(row,1,'-',border)
            worksheet.write(row,2,'-'),border
            worksheet.write(row,3,'Total Deductions',border)
            worksheet.write(row,4,'-',border)
            row+=1
            
            worksheet.write(row,0,'Net Pay',border)
            r1=row+1
            m1='B'+str(r1)+':'+'E'+str(r1)
            worksheet.merge_range(m1,'-',border)
            row+=1

            worksheet.write(row,0,'Remark',border)
            worksheet.write(row,2,'-',border)
            row+=4

        # Close the workbook before sending the data.
        workbook.close()

        # Rewind the buffer.
        output.seek(0)

        # Set up the Http response.
        filename = 'PaySlip.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
# def employeePayslip(request):
#     response=HttpResponse(content_type='application/ms-excel')
#     object_list = Employee.objects.all()
#     w=csv.writer(response)
#     w.writerow(['Salary For The Month of December 2020'])
#     for e in object_list:
#         w.writerow(['Name of the Employee',e.name,'Days in the Month','31'])
#         w.writerow([' Designation ','-',' Worked Days ','31'])
#         w.writerow([' Department ','-',' Date of Joining ',e.joining_date])
#         w.writerow([' Earning','Deductions'])
#         w.writerow(['',' Gross','Payable','Provident Fund','-'])
#         w.writerow([' Basic Salary',' -','-','ESIC','-'])
#         w.writerow(['House Rent Allowance ',' -','-','Profession Tax','-'])
#         w.writerow(['Conveyance Allowance ',' -','-','Income Tax','-'])
#         w.writerow(['Medical Allowance ',' -','-','Misc.Deduction/ Salary Arrears','-'])
#         w.writerow(['Monthly Incentive ',' -','-','Loan','-'])
#         w.writerow(['Special Allowance',' -','-','','-'])
#         w.writerow(['Salary Arrear ',' -','-','','-'])
#         w.writerow(['Total',' -','-','Total Deductions','-'])
#         w.writerow(['Remarks','-'])
#         w.writerow([''])
#     response['Content-Disposition']='attachment; filename="Payslip.csv"'
#     return response



class PayrollListView(ListView):
    model = Payroll
    template_name = "payroll/payroll-list.html"
    context_object_name = 'payroll_list'

    def get_queryset(self):

        object_list = Payroll.objects.all().order_by("-salary_issued_date")
        return object_list


class SalaryPackageView(View):
    def get(self, request, *args, **kwargs):
        obj = SalaryPackage.objects.get(
            employee__official_email=kwargs.get('pk'))
        all = {
            "Name": obj.employee.name,
            "Joining_Date": obj.employee.joining_date,
            "Basic": obj.basic,
            "gross_monthly_salary": obj.gross_monthly_salary,
            # "Address": obj.address,
            # "DOB": obj.dob,
            # "Gender": obj.gender,
        }
        pdf = render_to_pdf('pdf/salary-package.html', all)
        return HttpResponse(pdf, content_type='application/pdf')

