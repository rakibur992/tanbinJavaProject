from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    # TemplateView.as_view(template_name="index.html")
    path('<str:company>', views.EmployeeListView.as_view(), name='employee-list'),
    path('export', views.ExportPayslipToXlxs.as_view(),
         name='ExportPayslipToXlxs'),
    path('export/<str:index>', views.EmployExportPayslipToXlxs.as_view(),
         name='EmpolyExportPayslipToXlxs'),
    #     path('employee/payslip',views.employeePayslip,name='employeePayslip'),
    path('employee/<str:pk>', views.EmployeeDetailView.as_view(),
         name='employee-detail'),
    path('exportanyemployee/<str:employee_slug>', views.AnyEmployExportPayslipToXlxs.as_view(),name='AnyEmployExportPayslipToXlxs'),   
    path('', views.EmployeeView.as_view(),
         name='employee'),
    path('generateEmployeePayroll/<str:email>', views.GenerateEmployeePayroll.as_view(),
         name='GenerateEmployeePayroll')


]
