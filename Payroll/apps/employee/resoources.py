from .models import Employee, TaxPayerType, SalaryPackage, Payroll
from django.contrib import admin
from import_export import resources
from import_export.fields import Field


class EmployeeAdminResource(resources.ModelResource):

    class Meta:

        model = Employee
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ['created_at', 'modified_at', 'official_email',
                            'company', 'name', 'tax_payer_type', 'joining_date']  # Let it had 'id'

class PayrollAdminResource(resources.ModelResource):

    mobile = Field(attribute='mobile_bill', column_name='mobile')

    class Meta:
        model = Payroll
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)

        import_id_fields = ["employee", "salary_issued_date"]
        fields = ("employee", "employee__joining_date", "basic", "house_rent", "conveyance", "medical_bill",
                  'mobile', "bonus", "providend_fund", 'gratuity', 'gross_monthly_salary')
        export_order = ("employee", "employee__joining_date", "basic", "house_rent", "conveyance", "medical_bill",
                        'mobile', "bonus", "providend_fund", 'gratuity', 'gross_monthly_salary')


class SalaryPackageAdminResource(resources.ModelResource):

    mobile = Field(attribute='mobile_bill', column_name='mobile')

    class Meta:
        model = SalaryPackage
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ["employee", "basic", "house_rent", "conveyance", "medical_bill",
                            "mobile_bill", "bonus", "providend_fund", 'gratuity', ]
        fields = ("employee", "basic", "house_rent", "conveyance", "medical_bill",
                  'mobile', "bonus", "providend_fund", 'gratuity', 'gross_monthly_salary')
        export_order = ("employee", "basic", "house_rent", "conveyance", "medical_bill",
                        'mobile', "bonus", "providend_fund", 'gratuity', 'gross_monthly_salary')


class EmployeeListFilter(admin.SimpleListFilter):
    # title = "Tax Payer Type"
    # defaule_value = None
    title = 'Tax Payer Type'
    parameter_name = 'tax_payer'

    def lookups(self, request, model_admin):
        list_of_tax_payer = []
        queryset = TaxPayerType.objects.all()
        for item in queryset:
            list_of_tax_payer.append((str(item.id), str(item.tax_payer)))

        return sorted(list_of_tax_payer, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        pass
        # if self.value():
        #     return queryset.filter(tax_payer_type_id=self.value())
        # return queryset

        # def value():
        #     value = super(EmployeeListFilter, self).value()

        #     if value is None:
        #         if self.defaule_value is None:
        #             first_item = TaxPayerType.objects.order_by("id").first()
        #             value = None if first_item is None else first_item.id
        #             self.defaule_value = value
        #         else:
        #             value = self.defaule_value
        #     return str(value)
