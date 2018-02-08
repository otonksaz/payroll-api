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
