from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.conf import settings
from .models import *
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .resoources import EmployeeAdminResource, SalaryPackageAdminResource, PayrollAdminResource
from related_admin import RelatedFieldAdmin

from django_seed import Seed

seeder = Seed.seeder()


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeAdminResource
    # company
    list_display = ("name", "tax_payer_type",
                    "official_email", "joining_date")
    list_filter = ("tax_payer_type",
                   ("joining_date", DateRangeFilter))


# admin.site.register(Employee, EmployeeAdmin)


@admin.register(SalaryPackage)
class SalaryPackageAdmin(ImportExportModelAdmin, RelatedFieldAdmin):
    resource_class = SalaryPackageAdminResource
    search_fields = ("employee__official_email",)
    list_display = ("employee", "employee__joining_date", "basic", "house_rent", "conveyance", "medical_bill",
                    "mobile_bill", "bonus", "providend_fund", 'gratuity', 'gross_monthly_salary')


@admin.register(Payroll)
class PayrollAdmin(ImportExportModelAdmin):
    resource = PayrollAdminResource
    search_fields = ("employee__official_email",)

    list_display = ("employee", "basic", "house_rent", "conveyance", "medical",
                    "mobile", "bonus", "providend_fund", "salary_issued_date")

    fields = ("employee","monthly_incentive", "salary_issued_date")
    list_filter = (
        ("salary_issued_date", DateRangeFilter),)
    order = ("id",)


class InvestmentCreditAdmin(admin.ModelAdmin):
    list_display = ("percentage", "amount")
    # fields = ("percentage", "amount")
    order = ("id",)


class InvestmentRebateRuleAdmin(admin.ModelAdmin):
    list_display = ("percentage", "amount")
    # fields = ("percentage", "amount")
    order = ("id",)


@admin.register(Grade)
class GradeAdmin(ImportExportModelAdmin):
    pass


@admin.register(TaxableIncome)
class TaxableIncomeAdmin(admin.ModelAdmin):
    list_display = ("sector", "percentage",
                    "monthly_allowance", "yearly_allowance")
    list_display_links = ("sector",)
    ordering = ("id",)


@admin.register(TaxRule)
class TaxRuleAdmin(admin.ModelAdmin):
    list_display = ("tax_percentage",
                    "tax_bracket")
    list_display_links = ("tax_percentage",)
    ordering = ("id",)


# admin.site.register(Timesheet)
# admin.site.register(Grade)
# admin.site.register(JobTitle)
# admin.site.register(EmployeeDesignation)
# admin.site.register(EmployeeGrade)
# admin.site.register(Facility)
# admin.site.register(EmployeeFacility)

# admin.site.register(EmployeeContract)
admin.site.register(EmployeeInvestment)
admin.site.register(TaxPayerType)
admin.site.register(FinancialYear)
admin.site.register(InvestmentCredit, InvestmentCreditAdmin)
admin.site.register(InvestmentRebateRule, InvestmentRebateRuleAdmin)
