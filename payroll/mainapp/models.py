from django.db import models
from django.db.models import Count
from django.utils import timezone


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

DAY_CHOICES= (
    (1, 'Monday'),
    (2, 'Tueday'),
    (3, 'Wednesday'),
    (4, 'Thrusday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday')
)

DAYSTATUS_CHOICES= (
    ('I', 'In'),
    ('O', 'Off')
)

GENDER_CHOICES= (
    ('M', 'Male'),
    ('F', 'Female')
)

MARITAL_CHOICES= (
    ('M', 'Married'),
    ('S', 'Single'),
    ('D', 'Divorced')
)

IDENTITY_CHOICES = (
    ('K', 'KTP'),
    ('S', 'SIM'),
    ('F', 'KITAS')
)

RELIGION_CHOICES= (
    ('IS', 'Islam'),
    ('KP', 'Kristen Protestan'),
    ('KK', 'Kristen Katolik'),
    ('BD', 'Budha'),
    ('HD', 'Hindu')
)

RELATIONSHIP_CHOICES = (
    ('AY', 'Ayah'),
    ('IB', 'Ibu'),
    ('AN', 'Anak'),
    ('SK', 'Saudara Kandung'),
    ('IS', 'Istri'),
    ('SU', 'Suami'),
    ('LN', 'Lainnya'),
)

PROFESSION_CHOICES = (
    ('01', 'Belum / Tidak Bekerja'),
    ('02', 'Mengurus Rumah Tangga'),
    ('03', 'Pelajar / Mahasiswa'),
    ('04', 'Pensiunan'),
    ('05', 'Pegawai Negeri Sipil'),
    ('06', 'Tentara Nasional Indonesia'),
    ('07', 'Kepolisian RI'),
    ('08', 'Perdagangan'),
    ('09', 'Petani / Pekebun'),
    ('10', 'Peternak'),
    ('11', 'Nelayan / Perikanan'),
    ('12', 'Industri'),
    ('13', 'Konstruksi'),
    ('14', 'Transportasi'),
    ('15', 'Karyawan Swasta'),
    ('16', 'Karyawan BUMN'),
    ('17', 'Karyawan BUMD'),
    ('18', 'Karyawan Honorer'),
    ('19', 'Buruh Harian Lepas'),
    ('20', 'Buruh Tani / Perkebunan'),
    ('21', 'Buruh Nelayan / Perikanan'),
    ('22', 'Buruh Peternakan'),
    ('23', 'Pembantu Rumah Tangga'),
    ('24', 'Tukang Cukur'),
    ('25', 'Tukang Listrik'),
    ('26', 'Tukang Batu'),
    ('27', 'Tukang Kayu'),
    ('28', 'Tukang Sol Sepatu'),
    ('29', 'Tukang Las / Pandai Besi'),
    ('30', 'Tukang Jahit'),
    ('31', 'Penata Rambut'),
    ('32', 'Penata Rias'),
    ('33', 'Penata Busana'),
    ('34', 'Mekanik'),
    ('35', 'Tukang Gigi'),
    ('36', 'Seniman'),
    ('37', 'Tabib'),
    ('38', 'Paraji'),
    ('39', 'Perancang Busana'),
    ('40', 'Penterjemah'),
    ('41', 'Imam Masjid'),
    ('42', 'Pendeta'),
    ('43', 'Pastur'),
    ('44', 'Wartawan'),
    ('45', 'Ustadz / Mubaligh'),
    ('46', 'Juru Masak'),
    ('47', 'Promotor Acara'),
    ('48', 'Anggota DPR - RI'),
    ('49', 'Anggota DPD'),
    ('50', 'Anggota BPK'),
    ('51', 'Presiden'),
    ('52', 'Wakil Presiden'),
    ('53', 'Anggota Mahkamah Konstitusi'),
    ('54', 'Anggota Kabinet / Kementerian'),
    ('55', 'Duta Besar'),
    ('56', 'Gubernur'),
    ('57', 'Wakil Gubernur'),
    ('58', 'Bupati'),
    ('59', 'Wakil Bupati'),
    ('60', 'Walikota'),
    ('61', 'Wakil Walikota'),
    ('62', 'Anggota DPRD Propinsi'),
    ('63', 'Anggota DPRD Kabupaten / Kota'),
    ('64', 'Dosen'),
    ('65', 'Guru'),
    ('66', 'Pilot'),
    ('67', 'Pengacara'),
    ('68', 'Notaris'),
    ('69', 'Arsitek'),
    ('70', 'Akuntan'),
    ('71', 'Konsultan'),
    ('72', 'Dokter'),
    ('73', 'Bidan'),
    ('74', 'Perawat'),
    ('75', 'Apoteker'),
    ('76', 'Psikiater / Psikolog'),
    ('77', 'Penyiar Televisi'),
    ('78', 'Penyiar Radio'),
    ('79', 'Pelaut'),
    ('80', 'Peneliti'),
    ('81', 'Sopir'),
    ('82', 'Pialang'),
    ('83', 'Paranormal'),
    ('84', 'Pedagang'),
    ('85', 'Perangkat Desa'),
    ('86', 'Kepala Desa'),
    ('87', 'Biarawati'),
    ('88', 'Wiraswasta'),
)

APPLICANTSTATUS_CHOICES = (
    ('01', 'Submitted'),
    ('02', 'Approved'),
    ('03', 'Rejected')
)

EMPLOYMENTSTATUS_CHOICES = (
    ('F', 'Fulltime'),
    ('C', 'Contract'),
    ('P', 'Probation')
)

ATTENDANCETYPE_CHOICES = (
    ('S', 'Shift'),
    ('F', 'Fixed')
)

ABSENTDECUCTION_CHOICES = (
    ('W', 'Working Days'),
    ('C', 'Calendar Days'),
    ('E', 'Custom Days')
)

TAXCONFIG_CHOICES = (
    ('G', 'Gross'),
    ('N', 'Nett')
)

TYPEOFSALARY_CHOICES = (
    ('D', 'Daily'),
    ('M', 'Monthly')
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
    multiplyFrom = models.DecimalField(max_digits=2, decimal_places=1)
    multiplyTo = models.DecimalField(max_digits=2, decimal_places=1)
    multiplyBy = models.DecimalField(max_digits=3, decimal_places=1)


class TaxSetup(models.Model):
    company=models.OneToOneField(Company,on_delete=models.CASCADE,primary_key=True)
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


class AbsentPattern (models.Model):
    patternCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    @property
    def noOfDaysIn(self):
        return self.absentPatternDtls.filter(dayStatus='I').count()

    @property
    def noOfDaysOff(self):
        return self.absentPatternDtls.filter(dayStatus='O').count()

    def __str__(self):
        return self.name


class AbsentPatternDtl (models.Model):
    absentPattern = models.ForeignKey(AbsentPattern, related_name='absentPatternDtls', on_delete=models.CASCADE)
    dayPeriod = models.IntegerField(choices=DAY_CHOICES)
    dayStatus =models.CharField(max_length=1, choices=DAYSTATUS_CHOICES)
    timeIn = models.TimeField()
    timeOut = models.TimeField()
    breakIn = models.TimeField()
    breakOut = models.TimeField()


class Personal (models.Model):
    identityType = models.CharField(max_length=1, choices=IDENTITY_CHOICES)
    identityNo = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    mobilePhone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=10)
    placeBirth = models.CharField(max_length=100)
    dateBirth = models.DateField()
    marital = models.CharField(max_length=1,choices=MARITAL_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=2, choices=RELIGION_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('identityType', 'identityNo',)


class FamilyInfo(models.Model):
    personal = models.ForeignKey(Personal, related_name="familyInfos")
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP_CHOICES)
    dateBirth = models.DateField()
    marital = models.CharField(max_length=1, choices=MARITAL_CHOICES)
    occupation = models.CharField(max_length=2, choices=PROFESSION_CHOICES)


#Master for Education
class Institution(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Qualification(models.Model):
    qualificatioinCd = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#End Of Master for Education


class EducationInfo(models.Model):
    personal = models.ForeignKey(Personal, related_name="educationInfos")
    periodStart = models.IntegerField()
    periodEnd = models.IntegerField()
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    fieldOfStudy = models.ForeignKey(FieldOfStudy, on_delete=models.PROTECT)
    gpa = models.FloatField()

    def __str__(self):
        return self.institution.name


#Master for Career Info
class CompanyCareer(models.Model):
    companyCd = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#End of Master for Career Info


class CareerInfo(models.Model):
    personal = models.ForeignKey(Personal, related_name="careerInfos")
    companyCareer = models.ForeignKey(CompanyCareer, on_delete=models.PROTECT)
    jobPosition = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    jobLevel = models.ForeignKey(JobLevel, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=21, decimal_places=0)

    def __str__(self):
        return self.companyCareer.name


class Applicant(models.Model):
    jobPosition = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    jobLevel = models.ForeignKey(JobLevel, on_delete=models.PROTECT)
    personal = models.ForeignKey(Personal, on_delete=models.PROTECT)
    submittedDate = models.DateField(default=timezone.now)
    status = models.CharField(max_length=2, choices=APPLICANTSTATUS_CHOICES, default='01')

    def __str__(self):
        return self.personal.name


class Employee(models.Model):
    employeeId = models.CharField(max_length=25)
    applicant = models.ForeignKey(Applicant, on_delete=models.PROTECT)
    submittedDate = models.DateField(default=timezone.now)
    effectiveDate = models.DateField()
    jobPosition = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    jobLevel = models.ForeignKey(JobLevel, on_delete=models.PROTECT)
    email = models.EmailField()
    status = models.CharField(max_length=1, choices=EMPLOYMENTSTATUS_CHOICES)
    statusEnded = models.DateField(null=True, blank=True)
    attendanceType = models.CharField(max_length=1, choices=ATTENDANCETYPE_CHOICES)
    absentDeduct = models.CharField(max_length=1, choices=ABSENTDECUCTION_CHOICES)
    absentDeductCustom = models.IntegerField()
    absentPattern = models.ForeignKey(AbsentPattern, on_delete=models.PROTECT)
    isOvertime = models.BooleanField()
    overtime = models.ForeignKey(Overtime, on_delete=models.PROTECT, null=True, blank=True)
    payrollScheme = models.ForeignKey(PayrollScheme, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=21, decimal_places=0)
    taxConfig = models.CharField(max_length=1, choices=TAXCONFIG_CHOICES)
    salaryType = models.CharField(max_length=1, choices=TYPEOFSALARY_CHOICES)
    payrollBankName = models.CharField(max_length=100)
    payrollBankAcc = models.CharField(max_length=100)
    payrollBankAccName = models.CharField(max_length=100)
    taxTanggungan = models.IntegerField()
    npwp = models.CharField(max_length=25)

    def __str__(self):
        return self.applicant.personal.name


class Tax(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.PROTECT)
    ptkpPribadi = models.DecimalField(max_digits=21, decimal_places=0)
    ptkpIstri = models.DecimalField(max_digits=21, decimal_places=0)
    ptkpTanggungan = models.DecimalField(max_digits=21, decimal_places=0)
    maxTanggungan = models.IntegerField()
    isPembulatanRibuan = models.BooleanField()


class TaxCost(models.Model):
    tax = models.ForeignKey(Tax)
    yearlySalaryBottom = models.DecimalField(max_digits=21, decimal_places=0)
    yearlySalaryTop = models.DecimalField(max_digits=21, decimal_places=0)
    costNpwp = models.DecimalField(max_digits=6, decimal_places=2)
    costNonNpwp = models.DecimalField(max_digits=6, decimal_places=2)