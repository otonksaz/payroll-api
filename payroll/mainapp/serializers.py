from django.contrib.auth.models import User, Group, Permission
from django.db.models import Model
from rest_framework import serializers
from payroll.mainapp.models import *
from django.db.transaction import atomic


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = '__all__'


class ProRateSerializer(serializers.ModelSerializer):
    proRateValDescs = serializers.CharField(source='get_proRateVal_display', read_only=True)
    proRateDividerDescs = serializers.CharField(source='get_proRateDivider_display', read_only=True)

    class Meta:
        model = ProRate
        fields = '__all__'


class PayrollComponentDtlSerializer(serializers.ModelSerializer):
    calcTypeDescs = serializers.CharField(source='get_calcType_display', read_only=True)

    class Meta:
        model = PayrollComponentDtl
        fields = '__all__'
        extra_kwargs = {
            "payrollComponent": {
                "read_only": False,
                "required": False,
            }
        }


class PayrollComponentSerializer(serializers.ModelSerializer):
    calcTypeDescs = serializers.CharField(source='get_calcType_display', read_only=True)
    payrollComponentDtls = PayrollComponentDtlSerializer(many=True)


    class Meta:
        model = PayrollComponent
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        payrollComponentDtls_data = validated_data.pop('payrollComponentDtls')
        payrollComponent = PayrollComponent.objects.create(**validated_data)
        for payrollComponentDtl_data in payrollComponentDtls_data:
            PayrollComponentDtl.objects.create(payrollComponent=payrollComponent, **payrollComponentDtl_data)
        return payrollComponent

    @atomic()
    def update(self, instance, validated_data):
        instance.componentCd = validated_data.get('componentCd', instance.componentCd)
        instance.name = validated_data.get('name', instance.name)
        instance.calcType = validated_data.get('calcType', instance.calcType)
        instance.tax = validated_data.get('tax', instance.tax)
        instance.absentDeduct = validated_data.get('absentDeduct', instance.absentDeduct)
        instance.payrollDeduct = validated_data.get('payrollDeduct', instance.payrollDeduct)
        instance.compSubsidize = validated_data.get('compSubsidize', instance.compSubsidize)
        instance.proRate = validated_data.get('proRate', instance.proRate)
        instance.save()
        PayrollComponentDtl.objects.filter(payrollComponent=instance).delete()
        items = validated_data.get('payrollComponentDtls')

        if items:
            for item in items:
                item['payrollComponent'] = instance
                PayrollComponentDtl.objects.create(**item)
        return instance


class PayrollSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollScheme
        fields = '__all__'


class TimeOffPolicySerializer(serializers.ModelSerializer):
    resetByDescs = serializers.CharField(source='get_resetBy_display', read_only=True)

    class Meta:
        model = TimeOffPolicy
        fields = '__all__'


class PayrollSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollScheme
        fields = '__all__'

class TimeOffSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOffScheme
        fields = '__all__'


class OvertimeDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeDtl
        fields = '__all__'
        extra_kwargs = {
            "overtime": {
                "read_only": False,
                "required": False,
            }
        }


class OvertimeSerializer(serializers.ModelSerializer):
    overtimeDtls = OvertimeDtlSerializer(many=True)

    class Meta:
        model = Overtime
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        overtimeDtls_data = validated_data.pop('overtimeDtls')
        overtime = Overtime.objects.create(**validated_data)
        for overtimeDtl_data in overtimeDtls_data:
            OvertimeDtl.objects.create(overtime=overtime, **overtimeDtl_data)
        return overtime

    @atomic()
    def update(self, instance, validated_data):
        instance.overtimeCd = validated_data.get('overtimeCd', instance.overtimeCd)
        instance.name = validated_data.get('name', instance.name)
        instance.roundingMin = validated_data.get('roundingMin', instance.roundingMin)
        instance.save()
        OvertimeDtl.objects.filter(overtime=instance).delete()
        items = validated_data.get('overtimeDtls')

        if items:
            for item in items:
                item['overtime'] = instance
                OvertimeDtl.objects.create(**item)
        return instance


class TaxSetupDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxSetupDtl
        fields = '__all__'
        extra_kwargs = {
            "taxSetup": {
                "read_only": False,
                "required": False,
            }
        }


class TaxSetupSerializer(serializers.ModelSerializer):
    taxSetupDtls = TaxSetupDtlSerializer(many=True)
    companyName = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = TaxSetup
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        taxSetupDtls_data = validated_data.pop('taxSetupDtls')
        taxSetup = TaxSetup.objects.create(**validated_data)
        for taxSetupDtl_data in taxSetupDtls_data:
            TaxSetupDtl.objects.create(taxSetup=taxSetup, **taxSetupDtl_data)
        return taxSetup

    @atomic()
    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.company)
        instance.ptkpPribadi = validated_data.get('ptkpPribadi', instance.ptkpPribadi)
        instance.ptkpIstri = validated_data.get('ptkpIstri', instance.ptkpIstri)
        instance.ptkpTanggungan = validated_data.get('ptkpTanggungan', instance.ptkpTanggungan)
        instance.maxTanggungan = validated_data.get('maxTanggungan', instance.maxTanggungan)
        instance.rounding = validated_data.get('rounding', instance.rounding)
        instance.save()
        TaxSetupDtl.objects.filter(taxSetup=instance).delete()
        items = validated_data.get('taxSetupDtls')

        if items:
            for item in items:
                item['taxSetup'] = instance
                TaxSetupDtl.objects.create(**item)
        return instance


class AbsentPatternDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsentPatternDtl
        fields = '__all__'
        extra_kwargs = {
            "absentPattern": {
                "read_only": False,
                "required": False,
            }
        }


class AbsentPatternSerializer(serializers.ModelSerializer):
    absentPatternDtls = AbsentPatternDtlSerializer(many=True)
    noOfDaysIn = serializers.ReadOnlyField()
    noOfDaysOff = serializers.ReadOnlyField()

    class Meta:
        model = AbsentPattern
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        absentPatternDtls_data = validated_data.pop('absentPatternDtls')
        absentPattern = AbsentPattern.objects.create(**validated_data)
        for absentPatternDtl_data in absentPatternDtls_data:
            AbsentPatternDtl.objects.create(absentPattern=absentPattern, **absentPatternDtl_data)
        return absentPattern

    @atomic()
    def update(self, instance, validated_data):
        instance.dayPeriod = validated_data.get('dayPeriod', instance.dayPeriod)
        instance.dayStatus = validated_data.get('dayStatus', instance.dayStatus)
        instance.timeIn = validated_data.get('timeIn', instance.timeIn)
        instance.timeOut = validated_data.get('timeOut', instance.timeOut)
        instance.breakIn = validated_data.get('breakIn', instance.breakIn)
        instance.breakOut = validated_data.get('breakOut', instance.breakOut)
        instance.absentPattern = validated_data.get('absentPattern', instance.absentPattern)
        instance.save()
        AbsentPatternDtl.objects.filter(absentPattern=instance).delete()
        items = validated_data.get('absentPatternDtls')

        if items:
            for item in items:
                item['absentPattern'] = instance
                AbsentPatternDtl.objects.create(**item)
        return instance


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'


class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = '__all__'


class FamilyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInfo
        fields = '__all__'
        extra_kwargs = {
            "personal": {
                "read_only": False,
                "required": False,
            }
        }


class EducationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationInfo
        fields = '__all__'
        extra_kwargs = {
            "personal": {
                "read_only": False,
                "required": False,
            }
        }


class CompanyCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCareer
        fields = '__all__'


class CareerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerInfo
        fields = '__all__'
        extra_kwargs = {
            "personal": {
                "read_only": False,
                "required": False,
            }
        }


class PersonalSerializer(serializers.ModelSerializer):
    familyInfos = FamilyInfoSerializer(many=True)
    educationInfos = EducationInfoSerializer(many=True)
    careerInfos = CareerInfoSerializer(many=True)

    class Meta:
        model = Personal
        fields = '__all__'
        extra_kwargs = {
            "id": {
                "read_only": False
            }
        }

    def get_unique_together_validators(self):
        #Overriding method to disable unique together checks
        return []

    @atomic()
    def create(self, validated_data):
        fis = validated_data.pop('familyInfos')
        eis = validated_data.pop('educationInfos')
        cis = validated_data.pop('careerInfos')

        # get last id
        lastPersonal = Personal.objects.all().order_by('id').last()
        if not lastPersonal:
            validated_data["id"] = 1
        personalId = lastPersonal.id
        personalIdInt = int(personalId)
        newId = personalIdInt + 1
        validated_data["id"] = newId

        personal = Personal.objects.create(**validated_data)

        for fi in fis:
            FamilyInfo.objects.create(personal=personal, **fi)

        for ei in eis:
            EducationInfo.objects.create(personal=personal, **ei)

        for ci in cis:
            CareerInfo.objects.create(personal=personal, **ci)

        return personal

    @atomic()
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.mobilePhone = validated_data.get('mobilePhone', instance.mobilePhone)
        instance.email = validated_data.get('email', instance.email)
        instance.identityType = validated_data.get('identityType', instance.identityType)
        instance.identityNo = validated_data.get('identityNo', instance.identityNo)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.postal = validated_data.get('postal', instance.postal)
        instance.placeBirth = validated_data.get('placeBirth', instance.placeBirth)
        instance.dateBirth = validated_data.get('dateBirth', instance.dateBirth)
        instance.marital = validated_data.get('marital', instance.marital)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.save()

        instance.familyInfos.all().delete()
        instance.educationInfos.all().delete()
        instance.careerInfos.all().delete()

        fis = validated_data.get('familyInfos')
        eis = validated_data.get('educationInfos')
        cis = validated_data.get('careerInfos')

        for fi in fis:
            FamilyInfo.objects.create(personal=instance, **fi)

        for ei in eis:
            EducationInfo.objects.create(personal=instance, **ei)

        for ci in cis:
            CareerInfo.objects.create(personal=instance, **ci)

        return instance


class ApplicantSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer(required=True, partial=True)

    class Meta:
        model = Applicant
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        currentPersonal = Personal()
        newPersonal = validated_data.pop('personal')
        #print(newPersonal)

        if newPersonal["id"] != 0:
            currentPersonal = Personal.objects.filter(pk=newPersonal["id"]).first()
            if currentPersonal is not None:
                if currentPersonal.identityType != newPersonal["identityType"] or \
                        currentPersonal.identityNo != newPersonal["identityNo"]:
                    raise KeyError("Data personal is not valid")
                currentPersonal = PersonalSerializer.update(PersonalSerializer(), currentPersonal, validated_data=newPersonal)
            else:
                currentPersonal = PersonalSerializer.create(PersonalSerializer(), validated_data=newPersonal)
        else:
            currentPersonal = PersonalSerializer.create(PersonalSerializer(), validated_data=newPersonal)

        applicant = Applicant.objects.create(personal=currentPersonal, **validated_data)
        return applicant

    @atomic()
    def update(self, instance, validated_data):
        currentPersonal = Personal()
        newPersonal = validated_data.get('personal', None)
        print(newPersonal)

        if newPersonal["id"] != 0:
            currentPersonal = Personal.objects.filter(pk=newPersonal["id"]).first()
            if currentPersonal is not None:
                if currentPersonal.identityType != newPersonal["identityType"] or \
                        currentPersonal.identityNo != newPersonal["identityNo"]:
                    raise KeyError("Data personal is not valid")
                currentPersonal = PersonalSerializer.update(PersonalSerializer(), currentPersonal,
                                                            validated_data=newPersonal)
            #else:
            #    currentPersonal = PersonalSerializer.create(PersonalSerializer(), validated_data=newPersonal)

        instance.jobPosition = validated_data.get('jobPosition', instance.jobPosition)
        instance.jobLevel = validated_data.get('jobLevel', instance.jobLevel)
        instance.personal = currentPersonal
        # instance.submittedDate = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)

        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    applicant_data = ApplicantSerializer(source="applicant", read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'


class TaxCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCost
        fields = '__all__'
