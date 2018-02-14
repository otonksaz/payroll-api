from django.db import models


CALCTYPE_CHOICES = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly')
)

CALC_CHOICES = (
    ('A', 'Amount'),
    ('P', 'Percentage'),
)

OVER_CHOICES= (
    ('N', 'Weekday'),
    ('H', 'Weekend/Holiday'),
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
    calcType = models.CharField(max_length=1, choices=CALCTYPE_CHOICES)
    tax = models.BooleanField(default=True)
    absentDeduct = models.BooleanField(default=True)
    payrollDeduct = models.BooleanField(default=True)
    compSubsidize = models.BooleanField()
    proRate = models.ForeignKey(ProRate, on_delete=models.PROTECT, blank=True, null=True)

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
    payrollComponent=models.ManyToManyField(PayrollComponent)

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
    timeOffPolicy = models.ManyToManyField(TimeOffPolicy)

    def __str__(self):
        return self.name

class Overtime(models.Model):
    overtimeCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    roundingMin = models.IntegerField()

    def __str__(self):
        return self.name

class OvertimeDtl(models.Model):
    overtime = models.ForeignKey(Overtime,related_name='overtimeDtls', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=OVER_CHOICES)
    multplyFrom = models.DecimalField(max_digits=2, decimal_places=1)
    multplyTo = models.DecimalField(max_digits=2, decimal_places=1)
    multplyBy = models.DecimalField(max_digits=3, decimal_places=1)

class TaxSetup(models.Model):
    company=models.ForeignKey(Company, unique=True)
    ptkpPribadi = models.DecimalField(max_digits=12, decimal_places=0)
    ptkpIstri = models.DecimalField(max_digits=12, decimal_places=0)
    ptkpTanggungan = models.DecimalField(max_digits=12, decimal_places=0)
    maxTanggungan = models.IntegerField()
    rounding = models.BooleanField()

    def __str__(self):
        return u'%s %s' % ('Tax-', self.company)

class TaxSetupDtl(models.Model):
    taxSetup = models.ForeignKey(TaxSetup,related_name='taxSetupDtls', on_delete=models.CASCADE)
    salaryBottom = models.DecimalField(max_digits=12, decimal_places=0)
    salaryTop = models.DecimalField(max_digits=12, decimal_places=0)
    taxNpwp = models.DecimalField(max_digits=3, decimal_places=1)
    taxNonNpwp = models.DecimalField(max_digits=3, decimal_places=1)