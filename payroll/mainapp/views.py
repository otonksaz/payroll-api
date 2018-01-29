from rest_framework import viewsets
from django.contrib.auth.models import User, Group, Permission
from payroll.mainapp.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobLevelViewSet(viewsets.ModelViewSet):
    queryset = JobLevel.objects.all()
    serializer_class = JobLevelSerializer


class PayrollComponentViewSet(viewsets.ModelViewSet):
    queryset = PayrollComponent.objects.all()
    serializer_class = PayrollComponentSerializer


class PayrollComponentDtlViewSet(viewsets.ModelViewSet):
    queryset = PayrollComponentDtl.objects.all()
    serializer_class = PayrollComponentDtlSerializer


class ProRateViewSet(viewsets.ModelViewSet):
    queryset = ProRate.objects.all()
    serializer_class = ProRateSerializer