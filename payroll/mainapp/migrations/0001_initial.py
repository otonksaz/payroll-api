# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-25 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbsentPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patternCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AbsentPatternDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayPeriod', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tueday'), (3, 'Wednesday'), (4, 'Thrusday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('dayStatus', models.CharField(choices=[('I', 'In'), ('O', 'Off')], max_length=1)),
                ('timeIn', models.TimeField()),
                ('timeOut', models.TimeField()),
                ('breakIn', models.TimeField()),
                ('breakOut', models.TimeField()),
                ('absentPattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absentPatternDtls', to='mainapp.AbsentPattern')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submittedDate', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('01', 'Submitted'), ('02', 'Approved'), ('03', 'Rejected')], default='01', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CareerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=0, max_digits=21)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCareer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCd', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisionCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('descs', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodStart', models.IntegerField()),
                ('periodEnd', models.IntegerField()),
                ('gpa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.CharField(max_length=25)),
                ('submittedDate', models.DateField(default=django.utils.timezone.now)),
                ('effectiveDate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('F', 'Fulltime'), ('C', 'Contract'), ('P', 'Probation')], max_length=1)),
                ('statusEnded', models.DateField(blank=True, null=True)),
                ('attendanceType', models.CharField(choices=[('S', 'Shift'), ('F', 'Fixed')], max_length=1)),
                ('absentDeduct', models.CharField(choices=[('W', 'Working Days'), ('C', 'Calendar Days'), ('E', 'Custom Days')], max_length=1)),
                ('absentDeductCustom', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=0, max_digits=21)),
                ('taxConfig', models.CharField(choices=[('G', 'Gross'), ('N', 'Nett')], max_length=1)),
                ('salaryType', models.CharField(choices=[('D', 'Daily'), ('M', 'Monthly')], max_length=1)),
                ('payrollBankName', models.CharField(max_length=100)),
                ('payrollBankAcc', models.CharField(max_length=100)),
                ('payrollBankAccName', models.CharField(max_length=100)),
                ('taxTanggungan', models.IntegerField()),
                ('npwp', models.CharField(max_length=25)),
                ('absentPattern', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.AbsentPattern')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('relationship', models.CharField(choices=[('AY', 'Ayah'), ('IB', 'Ibu'), ('AN', 'Anak'), ('SK', 'Saudara Kandung'), ('IS', 'Istri'), ('SU', 'Suami'), ('LN', 'Lainnya')], max_length=2)),
                ('dateBirth', models.DateField()),
                ('marital', models.CharField(choices=[('M', 'Married'), ('S', 'Single'), ('D', 'Divorced')], max_length=1)),
                ('occupation', models.CharField(choices=[('01', 'Belum / Tidak Bekerja'), ('02', 'Mengurus Rumah Tangga'), ('03', 'Pelajar / Mahasiswa'), ('04', 'Pensiunan'), ('05', 'Pegawai Negeri Sipil'), ('06', 'Tentara Nasional Indonesia'), ('07', 'Kepolisian RI'), ('08', 'Perdagangan'), ('09', 'Petani / Pekebun'), ('10', 'Peternak'), ('11', 'Nelayan / Perikanan'), ('12', 'Industri'), ('13', 'Konstruksi'), ('14', 'Transportasi'), ('15', 'Karyawan Swasta'), ('16', 'Karyawan BUMN'), ('17', 'Karyawan BUMD'), ('18', 'Karyawan Honorer'), ('19', 'Buruh Harian Lepas'), ('20', 'Buruh Tani / Perkebunan'), ('21', 'Buruh Nelayan / Perikanan'), ('22', 'Buruh Peternakan'), ('23', 'Pembantu Rumah Tangga'), ('24', 'Tukang Cukur'), ('25', 'Tukang Listrik'), ('26', 'Tukang Batu'), ('27', 'Tukang Kayu'), ('28', 'Tukang Sol Sepatu'), ('29', 'Tukang Las / Pandai Besi'), ('30', 'Tukang Jahit'), ('31', 'Penata Rambut'), ('32', 'Penata Rias'), ('33', 'Penata Busana'), ('34', 'Mekanik'), ('35', 'Tukang Gigi'), ('36', 'Seniman'), ('37', 'Tabib'), ('38', 'Paraji'), ('39', 'Perancang Busana'), ('40', 'Penterjemah'), ('41', 'Imam Masjid'), ('42', 'Pendeta'), ('43', 'Pastur'), ('44', 'Wartawan'), ('45', 'Ustadz / Mubaligh'), ('46', 'Juru Masak'), ('47', 'Promotor Acara'), ('48', 'Anggota DPR - RI'), ('49', 'Anggota DPD'), ('50', 'Anggota BPK'), ('51', 'Presiden'), ('52', 'Wakil Presiden'), ('53', 'Anggota Mahkamah Konstitusi'), ('54', 'Anggota Kabinet / Kementerian'), ('55', 'Duta Besar'), ('56', 'Gubernur'), ('57', 'Wakil Gubernur'), ('58', 'Bupati'), ('59', 'Wakil Bupati'), ('60', 'Walikota'), ('61', 'Wakil Walikota'), ('62', 'Anggota DPRD Propinsi'), ('63', 'Anggota DPRD Kabupaten / Kota'), ('64', 'Dosen'), ('65', 'Guru'), ('66', 'Pilot'), ('67', 'Pengacara'), ('68', 'Notaris'), ('69', 'Arsitek'), ('70', 'Akuntan'), ('71', 'Konsultan'), ('72', 'Dokter'), ('73', 'Bidan'), ('74', 'Perawat'), ('75', 'Apoteker'), ('76', 'Psikiater / Psikolog'), ('77', 'Penyiar Televisi'), ('78', 'Penyiar Radio'), ('79', 'Pelaut'), ('80', 'Peneliti'), ('81', 'Sopir'), ('82', 'Pialang'), ('83', 'Paranormal'), ('84', 'Pedagang'), ('85', 'Perangkat Desa'), ('86', 'Kepala Desa'), ('87', 'Biarawati'), ('88', 'Wiraswasta')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overtimeCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('roundingMin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OvertimeDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('N', 'Weekday'), ('H', 'Weekend/Holiday')], max_length=1)),
                ('multiplyFrom', models.DecimalField(decimal_places=1, max_digits=2)),
                ('multiplyTo', models.DecimalField(decimal_places=1, max_digits=2)),
                ('multiplyBy', models.DecimalField(decimal_places=1, max_digits=3)),
                ('overtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overtimeDtls', to='mainapp.Overtime')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('calcType', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], max_length=1)),
                ('tax', models.BooleanField(default=True)),
                ('absentDeduct', models.BooleanField(default=True)),
                ('payrollDeduct', models.BooleanField(default=True)),
                ('compSubsidize', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PayrollComponentDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descs', models.CharField(max_length=150)),
                ('calcType', models.CharField(choices=[('A', 'Amount'), ('P', 'Percentage')], max_length=1)),
                ('maxSalaryCalc', models.DecimalField(decimal_places=2, max_digits=21)),
                ('employeeVAl', models.DecimalField(decimal_places=2, max_digits=21)),
                ('companyVal', models.DecimalField(decimal_places=2, max_digits=21)),
                ('payrollComponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrollComponentDtls', to='mainapp.PayrollComponent')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemeCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('payrollComponent', models.ManyToManyField(to='mainapp.PayrollComponent')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobilePhone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('identityType', models.CharField(choices=[('K', 'KTP'), ('S', 'SIM'), ('F', 'KITAS')], max_length=1)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('postal', models.CharField(max_length=10)),
                ('placeBirth', models.CharField(max_length=100)),
                ('dateBirth', models.DateField()),
                ('marital', models.CharField(choices=[('M', 'Married'), ('S', 'Single'), ('D', 'Divorced')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('religion', models.CharField(choices=[('IS', 'Islam'), ('KP', 'Kristen Protestan'), ('KK', 'Kristen Katolik'), ('BD', 'Budha'), ('HD', 'Hindu')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ProRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proRateCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('proRateVal', models.CharField(choices=[('W', 'Working Days'), ('C', 'Calendar Days')], max_length=1)),
                ('proRateDivCus', models.IntegerField()),
                ('proRateDivider', models.CharField(choices=[('W', 'Working Days'), ('C', 'Calendar Days'), ('X', 'Custom')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificatioinCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptkpPribadi', models.DecimalField(decimal_places=0, max_digits=21)),
                ('ptkpIstri', models.DecimalField(decimal_places=0, max_digits=21)),
                ('ptkpTanggungan', models.DecimalField(decimal_places=0, max_digits=21)),
                ('maxTanggungan', models.IntegerField()),
                ('isPembulatanRibuan', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearlySalaryBottom', models.DecimalField(decimal_places=0, max_digits=21)),
                ('yearlySalaryTop', models.DecimalField(decimal_places=0, max_digits=21)),
                ('costNpwp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('costNonNpwp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Tax')),
            ],
        ),
        migrations.CreateModel(
            name='TaxSetupDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaryBottom', models.DecimalField(decimal_places=0, max_digits=12)),
                ('salaryTop', models.DecimalField(decimal_places=0, max_digits=12)),
                ('taxNpwp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('taxNonNpwp', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOffPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOffCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('resetBy', models.CharField(choices=[('J', 'Join Date'), ('E', 'Expiry'), ('F', 'First Day Of Year'), ('C', 'Custom Date')], max_length=1)),
                ('customDate', models.DateField()),
                ('timeOffVal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeOffScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemeCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('timeOffPolicy', models.ManyToManyField(to='mainapp.TimeOffPolicy')),
            ],
        ),
        migrations.CreateModel(
            name='TaxSetup',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.Company')),
                ('ptkpPribadi', models.DecimalField(decimal_places=0, max_digits=12)),
                ('ptkpIstri', models.DecimalField(decimal_places=0, max_digits=12)),
                ('ptkpTanggungan', models.DecimalField(decimal_places=0, max_digits=12)),
                ('maxTanggungan', models.IntegerField()),
                ('rounding', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='tax',
            name='companyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Company'),
        ),
        migrations.AddField(
            model_name='payrollcomponent',
            name='proRate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.ProRate'),
        ),
        migrations.AddField(
            model_name='familyinfo',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Personal'),
        ),
        migrations.AddField(
            model_name='employee',
            name='isOvertime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.Overtime'),
        ),
        migrations.AddField(
            model_name='employee',
            name='jobLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobLevel'),
        ),
        migrations.AddField(
            model_name='employee',
            name='jobPosition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobPosition'),
        ),
        migrations.AddField(
            model_name='employee',
            name='payrollScheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.PayrollScheme'),
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='fieldOfStudy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.FieldOfStudy'),
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Institution'),
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Personal'),
        ),
        migrations.AddField(
            model_name='careerinfo',
            name='companyCareer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.CompanyCareer'),
        ),
        migrations.AddField(
            model_name='careerinfo',
            name='jobLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobLevel'),
        ),
        migrations.AddField(
            model_name='careerinfo',
            name='jobPosition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobPosition'),
        ),
        migrations.AddField(
            model_name='careerinfo',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Personal'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='jobLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobLevel'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='jobPosition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.JobPosition'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Personal'),
        ),
        migrations.AddField(
            model_name='taxsetupdtl',
            name='taxSetup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxSetupDtls', to='mainapp.TaxSetup'),
        ),
    ]
