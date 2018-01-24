from django.db import models


INTERVAL_CHOICES = (
        ('D', 'Day'),
        ('M', 'Month'),
        ('Y', 'Year')
    )

CALC_CHOICES = (
        ('A', 'Amount'),
        ('P', 'Percentage'),
    )


class Company(models.Model):
    companyCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Division(models.Model):
    divisionCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    descs = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class JobPosition(models.Model):
    positionCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JobLevel(models.Model):
    levelCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PayrollComponent(models.Model):
    componentCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    intervalType = models.CharField(max_length=1, choices=INTERVAL_CHOICES)
    proRate = models.BooleanField(default=True)
    proRateVal = models.IntegerField()
    tax = models.BooleanField(default=True)
    absentDeduct = models.BooleanField(default=True)
    payrollDeduct = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PayrollComponentDtl(models.Model):
    payrollComponent = models.ForeignKey(PayrollComponent, related_name='payrollcomponentdtls')
    descs = models.CharField(max_length=150)
    calcType = models.CharField(max_length=1, choices=CALC_CHOICES)
    amount = models.DecimalField(max_digits=21,decimal_places=2)
    companyExpense = models.DecimalField(max_digits=21,decimal_places=2)