from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Country(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    
    
class Location(models.Model):
    street_address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    
class Job(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    min_monthly_salary = models.DecimalField(max_digits=8, decimal_places=2)
    max_monthly_salary = models.DecimalField(max_digits=8, decimal_places=2)


class Employee(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    hire_date = models.DateField()
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    comission_pct = models.DecimalField(max_digits=4, decimal_places=4, null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True) # change manager when department is changed in signals
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True) # will add on_change in signals
    
    
class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='dep_manager') # add on_change to department employees in signals
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    
class JobHistory(models.Model):
    # This will be used in employee promotion, transfer or service ending form and will signal employee
    class Meta:
        unique_together = (('employee', 'start_date'),)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    job = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
class JobGrade(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=2, null=False, unique=True)
    lowest_sal = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    highest_sal = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    
