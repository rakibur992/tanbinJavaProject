
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from Payroll.apps.core.models import BaseModel
# from Payroll.apps.employee.models import Employee


class Company(BaseModel):
    name = models.CharField(primary_key=True,max_length=100)
    address = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    earning_attr = models.CharField(max_length=100, blank=True)
    deduction_attr = models.CharField(max_length=100, blank=True)
    company_logo=models.ImageField(null=True,blank=True)
    

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Role(models.Model):
    '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
    SUPER_ADMIN = 1
    ADMIN = 2
    IT_ADMIN = 3

    ROLE_CHOICES = (
        (SUPER_ADMIN, 'super_admin'),
        (IT_ADMIN, 'it_admin'),
        (ADMIN, 'admin'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.get_id_display()

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


# class CompanyAdmin(BaseModel):
#     company = models.ForeignKey(Company)
#     employee = models.ForeignKey(Employee)
#     role = models.ForeignKey(Role)
