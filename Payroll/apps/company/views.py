from .models import *
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = "company/company-list.html"
    context_object_name = 'company_list'
    def get_queryset(self):

        object_list = Company.objects.all()
        return object_list