from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    # TemplateView.as_view(template_name="index.html")
    path('', views.CompanyListView.as_view(), name='company-list'),
    path('company/', include('Payroll.apps.employee.urls')),
     
]
