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

PRORATEVAL_CHOICES = (
    ('W', 'Working Days'),
    ('C', 'Calendar Days'),
)

PRORATEDIVIDER_CHOICES = (
    ('W', 'Working Days'),
    ('C', 'Calendar Days'),
    ('X', 'Custom'),
)

TIMEOFFRESET_CHOICES = (
    ('J', 'Join Date'),
    ('E', 'Expiry'),
    ('F', 'First Day Of Year'),
    ('C', 'Custom Date'),
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


class ProRate(models.Model):
    proRateCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    proRateVal = models.CharField(max_length=1, choices=PRORATEVAL_CHOICES)
    proRateDivCus = models.IntegerField()
    proRateDivider = models.CharField(max_length=1, choices=PRORATEDIVIDER_CHOICES)

    def __str__(self):
        return self.name


class PayrollComponent(models.Model):
    componentCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    intervalType = models.CharField(max_length=1, choices=INTERVAL_CHOICES)
    tax = models.BooleanField(default=True)
    absentDeduct = models.BooleanField(default=True)
    payrollDeduct = models.BooleanField(default=True)
    compSubsidize = models.BooleanField()
    proRate = models.ForeignKey(ProRate, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class PayrollComponentDtl(models.Model):
    payrollComponent = models.ForeignKey(PayrollComponent, related_name='payrollComponentDtls', on_delete=models.CASCADE)
    descs = models.CharField(max_length=150)
    calcType = models.CharField(max_length=1, choices=CALC_CHOICES)
    maxSalaryCalc = models.DecimalField(max_digits=21,decimal_places=2)
    employeeVAl = models.DecimalField(max_digits=21,decimal_places=2)
    companyVal = models.DecimalField(max_digits=21,decimal_places=2)


class PayrollScheme(models.Model):
    schemeCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    payrollComponents = models.ManyToManyField(PayrollComponent)

    def __str__(self):
        return self.name


class TimeOffPolicy(models.Model):
    timeOffCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    resetBy = models.CharField(max_length=1, choices=TIMEOFFRESET_CHOICES)
    customDate = models.DateField()
    timeOffVal = models.IntegerField()

    def __str__(self):
        return self.name


class TimeOffScheme(models.Model):
    schemeCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    timeOffPolicies = models.ManyToManyField(TimeOffPolicy)