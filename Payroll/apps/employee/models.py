from django.db.models.signals import post_save
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from Payroll.apps.core.models import BaseModel
from Payroll.apps.user.models import User
from Payroll.apps.company.models import Company
from dateutil.relativedelta import relativedelta

# Create your models here.


class TaxPayerType(models.Model):

    MALE = 1
    FEMALE = 2
    FREEDOM_FIGHTER = 3
    PARENTS_OF_SPECIAL_CHILD = 4
    SPECIAL_CHILD = 5

    TaxPayer_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (FREEDOM_FIGHTER, 'freedom figter'),
        (PARENTS_OF_SPECIAL_CHILD, 'parents of sepcial child'),
        (SPECIAL_CHILD, 'special child'),

    )

    tax_payer = models.PositiveSmallIntegerField(
        choices=TaxPayer_CHOICES, default=0)
    max_non_taxable_amount = models.FloatField(default=0.0)
    # upper_limit
    notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        # + " - " + str(self.max_non_taxable_amount)
        # print(self.tax_payer)
        return str(self.TaxPayer_CHOICES[self.tax_payer-1][1]) + "-->" + str(self.max_non_taxable_amount)

    class Meta:
        verbose_name = 'Tax Payer Type'
        verbose_name_plural = 'Tax Payer Types'

    def save(self, *args, **kwargs):
        self.my_float = round(self.max_non_taxable_amount, 2)
        super(TaxPayerType, self).save(*args, **kwargs)


class Grade(BaseModel):
    grade = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.grade


class JobTitle(BaseModel):
    job_title = models.CharField(max_length=100, blank=True)
    job_description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.job_title


class Employee(BaseModel):

    official_email = models.CharField(
        primary_key=True, max_length=100, blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    # company = models.ForeignKey(
    #     Company, on_delete=models.CASCADE, related_name="employees")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True)
    tax_payer_type = models.ForeignKey(
        TaxPayerType, on_delete=models.CASCADE)
    basic = models.FloatField()
    house_rent = models.FloatField()
    medical_bill = models.FloatField()
    conveyance = models.FloatField()
    mobile_bill = models.FloatField(default=0.0)
    providend_fund = models.FloatField(default=0.0)
    gratuity = models.FloatField(default=0.0)
    bonus = models.FloatField(default=0.0)
    gross_monthly_salary = models.FloatField(default=0.0)
    comment = models.CharField(max_length=100, blank=True)

    joining_date = models.DateField()

    def __str__(self):
        return self.official_email

    def save(self, *args, **kwargs):
        self.gross_monthly_salary = self.basic + self.house_rent + self.medical_bill + \
            self.conveyance + self.mobile_bill + \
            self.providend_fund + self.gratuity
        super(Employee, self).save(*args, **kwargs)

def save_salary_package(sender, instance, **kwargs):

    SalaryPackage.objects.create(employee=instance, basic=instance.basic,
                                 house_rent=instance.house_rent, medical_bill=instance.medical_bill, conveyance=instance.conveyance, mobile_bill=instance.mobile_bill,
                                 providend_fund=instance.providend_fund, gratuity=instance.gratuity, bonus=instance.bonus, comment=instance.comment, last_increment_date=instance.joining_date)
    financial_year = FinancialYear.objects.get(current_year=True)
    EmployeeInvestment.objects.create(
        employee=instance, financial_year=financial_year, yearly_investment_amount=0)
    EmployeeTaxAdvencePayment.objects.create(employee=instance)

post_save.connect(save_salary_package, sender=Employee)

class EmployeeTaxAdvencePayment(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    advance_tax_paid_last_financial_year=models.FloatField(default=0.0)
    def __str__(self):
        return self.employee.name 

    class Meta:
        verbose_name = "Employee Tax Advence Payment"
        verbose_name_plural = "Employee Tax Advence Payments"

class EmployeeGrade(BaseModel):
    employee = models.OneToOneField(
        Employee, on_delete=models.PROTECT, to_field="official_email", db_column="official_email")
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT)
    promotion_date = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Employee Grade'
        verbose_name_plural = 'Employee Grades'


class EmployeeDesignation(BaseModel):
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)
    designation = models.OneToOneField(
        JobTitle, on_delete=models.PROTECT)
    promotion_date = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Employee Designation'
        verbose_name_plural = 'Employee Designations'


class Timesheet(BaseModel):
    employee_id = models.ForeignKey(Employee,
                                    on_delete=models.PROTECT)
    raw_time = models.CharField(max_length=100, blank=True)
    check_in = models.DateTimeField(blank=True)
    check_out = models.DateTimeField(blank=True)
    rounted_time = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.employee_id


class Facility(BaseModel):
    facility = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.facility

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class EmployeeFacility(BaseModel):
    grade = models.ManyToManyField(Grade)
    facility = models.ManyToManyField(Facility)

    def __str__(self):
        return self.grade + " : " + self.facility

    class Meta:
        verbose_name = 'Employee Facility'
        verbose_name_plural = 'Employee Facilities'


class Bonus(models.Model):
    bonus_1 = models.FloatField(blank=True)
    bonus_2 = models.FloatField(blank=True)
    bonus_3 = models.FloatField(blank=True)
    performance_bonus = models.FloatField(blank=True)
    project_bonus = models.FloatField(blank=True)
    other_bonus = models.FloatField(blank=True)


class EmployeeBonus(models.Model):
    BONUS_1 = 1
    BONUS_2 = 2
    BONUS_3 = 3
    BONUS_PERFORMANCE = 4
    BONUS_PROJECT = 5
    BONUS_OTHER = 6

    BONUS_CHOICES = (
        (BONUS_1, 'BONUS 1'),
        (BONUS_2, 'BONUS 2'),
        (BONUS_3, 'BONUS 3'),
        (BONUS_PERFORMANCE, 'BONUS PERFORMANCE'),
        (BONUS_PROJECT, 'BONUS PROJECT'),
        (BONUS_OTHER, 'BONUS OTHER'),

    )
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    bonus = models.PositiveSmallIntegerField(
        choices=BONUS_CHOICES, default=0)
    payment_date = models.DateField()

    def __str__(self):
        return self.employee.name


class FinancialYear(BaseModel):
    financial_year_start = models.DateField()
    financial_year_end = models.DateField()

    name = models.CharField(max_length=100, blank=True)
    current_year = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SalaryPackage(BaseModel):

    employee = models.ForeignKey(
        Employee,  on_delete=models.PROTECT, to_field="official_email", db_column="official_email")
    basic = models.FloatField(blank=True)
    house_rent = models.FloatField(blank=True)
    medical_bill = models.FloatField(blank=True)
    conveyance = models.FloatField(blank=True)
    mobile_bill = models.FloatField(blank=True)
    providend_fund = models.FloatField(blank=True)
    gratuity = models.FloatField(blank=True)
    bonus = models.FloatField(blank=True)
    special_allowence_7 = models.FloatField(blank=True,default=0.0)
    monthly_incentive = models.FloatField(default=0.0,blank=True)
    performance_bonus_given =  models.FloatField(default=0.0,blank=True)
    # investment = models.FloatField(blank=True)
    gross_monthly_salary = models.FloatField(blank=True)
    gross_yearly_salary = models.FloatField(blank=True)
    comment = models.CharField(max_length=100, blank=True)
    salary_this_year = models.FloatField(blank=True)
    total_salary_income = models.FloatField(blank=True)
    tax_paid_this_year_without_investment= models.FloatField(default=0.0,blank=True)
    tax_paid_this_year_with_rebate = models.FloatField(default=0.0,blank=True)
    last_increment_date = models.DateField(blank=True)

    def __str__(self):
        return self.employee.name + " " + str(self.gross_monthly_salary)

    class Meta:
        verbose_name = 'Salary Package'
        verbose_name_plural = 'Salary Packages'

    def save(self, *args, **kwargs):
        _employee = Employee.objects.get(
            pk=self.employee.official_email)
        _financial_year = FinancialYear.objects.get(current_year=True)
        _salaries_this_year = self.difference_in_months(_employee.joining_date,
                                                        _financial_year.financial_year_end)

        self.gross_monthly_salary = self.basic + self.house_rent + self.medical_bill + \
            self.conveyance + self.mobile_bill + \
            self.providend_fund + self.gratuity
        self.gross_yearly_salary = self.gross_monthly_salary * _salaries_this_year
        self.salary_this_year = _salaries_this_year
        
        self.total_salary_income = self.gross_yearly_salary + self.bonus+self.special_allowence_7+self.monthly_incentive+self.performance_bonus_given

        super(SalaryPackage, self).save(*args, **kwargs)

    def difference_in_months(self, start, end):
        months=round((end-start).days/30)
        if months > 11:
            return 12
        return months


class InvestmentRebateRule(BaseModel):
    financial_year = models.ForeignKey(FinancialYear, on_delete=models.PROTECT)
    percentage = models.FloatField(blank=True)
    amount = models.FloatField(blank=True)

    class Meta:
        verbose_name = 'Investment Rebate Rule'
        verbose_name_plural = 'Investment Rebate Rules'


class InvestmentCredit(BaseModel):
    financial_year = models.ForeignKey(FinancialYear, on_delete=models.PROTECT)
    percentage = models.FloatField(blank=True)
    amount = models.FloatField(blank=True)

    class Meta:
        verbose_name = "Investment Credit"


class EmployeeInvestment(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    financial_year = models.ForeignKey(FinancialYear, on_delete=models.PROTECT)
    yearly_investment_amount = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.employee.name + " " + str(self.financial_year) + " " + str(self.yearly_investment_amount)

    class Meta:
        verbose_name = "Employee Investment"
        verbose_name_plural = "Employee Investments"


class EmployeeContract(BaseModel):
    employee = models.ForeignKey(
        Employee,  on_delete=models.PROTECT, to_field="official_email", db_column="official_email")
    salary_package = models.ForeignKey(SalaryPackage, on_delete=models.PROTECT)
    contract_date = models.DateField()

    def __str__(self):
        return self.employee.official_email + " --> "+str(self.salary_package.gross_monthly_salary)

    class Meta:
        verbose_name = 'Employee Contract'
        verbose_name_plural = 'Employee Contracts'


class Payroll(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, to_field="official_email", db_column="official_email")

    salary_issued_date = models.DateField()
    basic = models.FloatField(blank=True, default=0.0)

    house_rent = models.FloatField(blank=True, default=0.0)
    house_rent_basic_pay_50 = models.FloatField(blank=True, default=0.0)
    house_rent_as_per_salary = models.FloatField(blank=True, default=0.0)
    house_rent_band = models.FloatField(blank=True, default=0.0)
    house_rent_exempt = models.FloatField(blank=True, default=0.0)

    conveyance = models.FloatField(blank=True, default=0.0)
    conveyance_as_per_salary = models.FloatField(blank=True, default=0.0)
    conveyance_band = models.FloatField(blank=True, default=0.0)
    conveyance_exempt = models.FloatField(blank=True, default=0.0)

    medical = models.FloatField(blank=True, default=0.0)
    medical_basic_pay_10 = models.FloatField(blank=True, default=0.0)
    medical_as_per_salary = models.FloatField(blank=True, default=0.0)
    medical_band = models.FloatField(blank=True, default=0.0)
    medical_exempt = models.FloatField(blank=True, default=0.0)

    mobile = models.FloatField(blank=True, default=0.0)
    bonus = models.FloatField(blank=True, default=0.0)
    monthly_incentive = models.FloatField(blank=True, default=0.0)
    special_allowence_7 = models.FloatField(blank=True, default=0.0)
    providend_fund = models.FloatField(blank=True, default=0.0)
    performance_bonus = models.FloatField(blank=True, default=0.0)
    gross_salary_this_month = models.FloatField(blank=True, default=0.0)
    net_salary_this_month = models.FloatField(blank=True, default=0.0)

    tax_1 = models.FloatField(blank=True, default=0.0)
    tax_2 = models.FloatField(blank=True, default=0.0)
    tax_3 = models.FloatField(blank=True, default=0.0)
    tax_4 = models.FloatField(blank=True, default=0.0)
    tax_5 = models.FloatField(blank=True, default=0.0)
    # tax_1 = models.FloatField(blank=True, default=0.0)

    yearly_taxable_income = models.FloatField(blank=True, default=0.0)
    yearly_tax_without_investment = models.FloatField(blank=True, default=0.0)

    investment_credit = models.FloatField(blank=True, default=0.0)
    investment_rebate = models.FloatField(blank=True, default=0.0)

    yearly_tax_with_investment_rebate = models.FloatField(
        blank=True, default=0.0)
    tax_this_month_without_investment = models.FloatField(
        blank=True, default=0.0)
    salary_this_month_without_investment = models.FloatField(
        blank=True, default=0.0)

    tax_this_month_with_rebate = models.FloatField(blank=True, default=0.0)
    salary_this_month_with_rebate = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.employee.official_email

    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'

    def less_among_three(self, a, b, c):
        return a if a < b and a < c else b if b < c else c
    def difference_in_months(self, start, end):

        months=round((end-start).days/30)
        return months

    def save(self, *args, **kwargs):

        _employee = Employee.objects.get(
            pk=self.employee.official_email)
        _employee_id = self.employee.official_email
        _financial_year = FinancialYear.objects.get(current_year=True)

        _salary_package = SalaryPackage.objects.filter(
            employee=_employee_id).order_by('-id').first()

        _salary_package.monthly_incentive += self.monthly_incentive 

        self.special_allowence_7 = round((_salary_package.basic *0.07),2) if \
            self.difference_in_months(_employee.joining_date,self.salary_issued_date) > 11 else 0
        _salary_package.special_allowence_7 += self.special_allowence_7

        _salary_package.performance_bonus_given += self.performance_bonus
        _salary_package.save()

        _salary_package = SalaryPackage.objects.filter(
            employee=_employee_id).order_by('-id').first()
            
        self.basic = _salary_package.basic if self.basic < 1 else self.basic
        self.house_rent = _salary_package.house_rent if self.house_rent < 1 else self.house_rent
        self.conveyance = _salary_package.conveyance if self.conveyance < 1 else self.conveyance
        self.medical = _salary_package.medical_bill if self.medical < 1 else self.medical
        self.bonus = _salary_package.bonus if self.bonus < 1 else self.bonus
        self.mobile = _salary_package.mobile_bill if self.mobile < 1 else self.mobile
        self.providend_fund = _salary_package.providend_fund if self.providend_fund < 1 else self.providend_fund
        _tax_exempt = TaxableIncome.objects.all()
        _medical = TaxableIncome.objects.get(sector='Medical')
        _house_rent = TaxableIncome.objects.get(sector='House Rent')
        _transport = TaxableIncome.objects.get(sector='Transport')
        # self.salary_package = _salary_package

        _investment_credit = InvestmentCredit.objects.all().order_by("id")
        _investment_rebate = InvestmentRebateRule.objects.all().order_by("id")

        try:
            _employee_actual_investment = EmployeeInvestment.objects.filter(
                employee=_employee_id).order_by("-id").first().yearly_investment_amount
        except EmployeeInvestment.DoesNotExist:
            _employee_actual_investment = 10000000.0
        
        # houserent exempt
        self.house_rent_basic_pay_50 = (_salary_package.basic *
                                        _salary_package.salary_this_year) / 2
        self.house_rent_as_per_salary = _salary_package.house_rent * \
            _salary_package.salary_this_year
        temp_house_rent_as_per_salary = _house_rent.monthly_allowance * _salary_package.salary_this_year

        self.house_rent_band = temp_house_rent_as_per_salary if temp_house_rent_as_per_salary < _house_rent.yearly_allowance else _house_rent.yearly_allowance  
        self.house_rent_exempt = self.less_among_three(
            self.house_rent_basic_pay_50, self.house_rent_as_per_salary, self.house_rent_band)

        # conveyance
        self.conveyance_as_per_salary = _salary_package.conveyance * \
            _salary_package.salary_this_year
        self.conveyance_band = _transport.yearly_allowance
        self.conveyance_exempt = self.less_among_three(
            1000000, self.conveyance_as_per_salary, self.conveyance_band)

        # medical exempt
        self.medical_basic_pay_10 = (_salary_package.basic *
                                     _salary_package.salary_this_year) / 10
        self.medical_as_per_salary = _salary_package.medical_bill * \
            _salary_package.salary_this_year
        # temp_medical_as_per_salary = _medical.monthly_allowance * _salary_package.salary_this_year
        self.medical_band =  _medical.yearly_allowance
        # temp_medical_as_per_salary if temp_medical_as_per_salary < else _medical.yearly_allowance
        self.medical_exempt = self.less_among_three(
            self.medical_basic_pay_10, self.medical_as_per_salary, self.medical_band)

        # yearly taxable income
        self.yearly_taxable_income = _salary_package.total_salary_income - \
            self.house_rent_exempt - self.conveyance_exempt - self.medical_exempt

        # yearly tax calculation without investment
        _max_limit = _employee.tax_payer_type.max_non_taxable_amount

        if self.yearly_taxable_income > _max_limit:
            _base_step = self.yearly_taxable_income - _max_limit
            print(_base_step)
            self._tax_deduct(_base_step)
        # this funtion returns self.yearlytax without invesment
        else:
            self.tax_1 = self.tax_2 = self.tax_3 = self.tax_4 = self.tax = 0
            self.yearly_tax_without_investment = 5000
        _advance_tax_paid_last_financial_year = EmployeeTaxAdvencePayment.objects.get(employee=_employee).advance_tax_paid_last_financial_year
        _tax_month_left = self.difference_in_months(self.salary_issued_date,_financial_year.financial_year_end)
        _tax_need_to_pay_this_year = self.yearly_tax_without_investment  - _salary_package.tax_paid_this_year_without_investment - _advance_tax_paid_last_financial_year

        self.tax_this_month_without_investment = round(_tax_need_to_pay_this_year/_tax_month_left, 2)
        _salary_package.tax_paid_this_year_without_investment += round(self.tax_this_month_without_investment,2)      

        self.gross_salary_this_month = _salary_package.gross_monthly_salary
        self.salary_this_month_without_investment = round(self.gross_salary_this_month -
                                                          self.tax_this_month_without_investment, 2)
        # yearly tax calculation with investment
        _investment_credit_per_salary = self.yearly_taxable_income / \
            100 * _investment_credit[0].percentage
        # investment Credit
        self.investment_credit = self.less_among_three(
            _investment_credit[0].amount, _investment_credit_per_salary, _employee_actual_investment)
        # investment rebate
        _investment_rebate_percentage = 15 if self.yearly_taxable_income <= 1500000 else 10
        # _investment_rebate[
        #     0].percentage if self.yearly_taxable_income <= _investment_rebate[0].amount else _investment_rebate[1].percentage

        self.investment_rebate = (
            self.investment_credit / 100) * _investment_rebate_percentage
    
        self.yearly_tax_with_investment_rebate = round(self.yearly_tax_without_investment -
                                                       self.investment_rebate, 2)
        _tax_need_to_pay_this_year_with_rebate = self.yearly_tax_with_investment_rebate - _salary_package.tax_paid_this_year_with_rebate -_advance_tax_paid_last_financial_year
    

        self.tax_this_month_with_rebate = round(
            _tax_need_to_pay_this_year_with_rebate  / _tax_month_left, 2)
        _salary_package.tax_paid_this_year_with_rebate += round(self.tax_this_month_with_rebate)
        _salary_package.save()
        # self.tax_this_month_with_rebate = round(
        #     self.yearly_tax_with_investment_rebate / _salary_package.salary_this_year, 2)
        self.salary_this_month_with_rebate = self.net_salary_this_month = round(self.gross_salary_this_month -
                                                                                self.tax_this_month_with_rebate, 2)
        super(Payroll, self).save(*args, **kwargs)

    def _tax_deduct(self, _base_step):

        _tax_percentage_1, _tax_bracket_1 = self._tax_rule(0)
        _money_1, _tax_1 = self._tax_calculation(
            _base_step, _tax_percentage_1, _tax_bracket_1)
        self.tax_1 = _tax_1 if _tax_1 > 0 else 0

        _tax_percentage_2, _tax_bracket_2 = self._tax_rule(1)
        _money_2, _tax_2 = self._tax_calculation(
            _money_1, _tax_percentage_2, _tax_bracket_2)
        self.tax_2 = _tax_2 if _tax_2 > 0 else 0

        _tax_percentage_3, _tax_bracket_3 = self._tax_rule(2)
        _money_3, _tax_3 = self._tax_calculation(
            _money_2, _tax_percentage_3, _tax_bracket_3)
        self.tax_3 = _tax_3 if _tax_3 > 0 else 0

        _tax_percentage_4, _tax_bracket_4 = self._tax_rule(3)
        _money_4, _tax_4 = self._tax_calculation(
            _money_3, _tax_percentage_4, _tax_bracket_4)
        self.tax_4 = _tax_4 if _tax_4 > 0 else 0

        _tax_percentage_5, _tax_bracket_5 = self._tax_rule(4)
        _money_5, _tax_5 = self._tax_calculation(
            _money_4, _tax_percentage_5, _tax_bracket_5)
        self.tax_5 = _tax_5 if _tax_5 > 0 else 0

        self. yearly_tax_without_investment = self.tax_1 + \
            self.tax_2 + self.tax_3 + self.tax_4 + self.tax_5
        
        if self.yearly_tax_without_investment <= 5000:
            self.yearly_tax_without_investment = 5000


    def _tax_calculation(self, _base, _tax_percentage, _tax_bracket):

        if _base <= 0:
            return 0, 0
        # 25% of rest of the amount
        if _tax_bracket == 1:
            _money = 0
            _tax = (_base / 100) * _tax_percentage
            return _money, _tax

        _money = _base - _tax_bracket
        if _money <= 0:
            _tax = (_base / 100) * _tax_percentage
            return 0, _tax

        _tax = (_tax_bracket / 100) * _tax_percentage

        return _money, _tax
    def _tax_rule(self, rule_number):
        _tax_rule = TaxRule.objects.all().order_by("id")
        return _tax_rule[rule_number].TAX_RULE_CHOICES[_tax_rule[rule_number].tax_percentage-1][1], _tax_rule[rule_number].tax_bracket


class HolidayLeave(BaseModel):
    casual_leave = models.IntegerField(blank=True)
    sick_leave = models.IntegerField(blank=True)
    holiday = models.IntegerField(blank=True)
    others = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Holiday Leave'
        verbose_name_plural = 'Holiday Leaves'


class TaxableIncome(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sector = models.CharField(max_length=100)
    percentage = models.FloatField(blank=True, default=0.0)
    monthly_allowance = models.FloatField(blank=True, default=0.0)
    yearly_allowance = models.FloatField(blank=True, default=0.0)
    rules = models.CharField(max_length=500, blank=True)
    notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.sector

    class Meta:
        verbose_name = 'Taxable Income'
        verbose_name_plural = 'Taxable Incomes'


class TaxRule(BaseModel):
    FIRST_BRACKET = 1
    SECOND_BRACKET = 2
    THIRD_BRACKET = 3
    FOURTH_BRACKET = 4
    LAST_BRACKET = 5

    TAX_RULE_CHOICES = (
        (FIRST_BRACKET, 5),
        (SECOND_BRACKET, 10),
        (THIRD_BRACKET, 15),
        (FOURTH_BRACKET, 20),
        (LAST_BRACKET, 25),

    )
    tax_percentage = models.PositiveSmallIntegerField(
        choices=TAX_RULE_CHOICES, default=0)
    tax_bracket = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Tax Rule'
        verbose_name_plural = 'Tax Rules'

    # def __str__(self):
    #     return str(self.TAX_RULE_CHOICES[self.id-1][1]) + "% tax on next " + str(self.tax_bracket)
