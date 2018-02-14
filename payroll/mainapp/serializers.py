from django.contrib.auth.models import User, Group, Permission
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
    class Meta:
        model = ProRate
        fields = '__all__'


class PayrollComponentDtlSerializer(serializers.ModelSerializer):
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
        instance.intervalType = validated_data.get('intervalType', instance.intervalType)
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


class TimeOffPolicySerializer(serializers.ModelSerializer):
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
            "Overtime": {
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
            "TaxSetup": {
                "read_only": False,
                "required": False,
            }
        }

class TaxSetupSerializer(serializers.ModelSerializer):
    taxSetupDtls = TaxSetupDtlSerializer(many=True)


    class Meta:
        model = TaxSetup
        fields = '__all__'

    @atomic()
    def create(self, validated_data):
        taxSetupDtls_data = validated_data.pop('taxSetupDtls')
        taxSetup = Overtime.objects.create(**validated_data)
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