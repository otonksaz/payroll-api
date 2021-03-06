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


class TimeOffPolicyViewSet(viewsets.ModelViewSet):
    queryset = TimeOffPolicy.objects.all()
    serializer_class = TimeOffPolicySerializer


class PayrollSchemeViewSet(viewsets.ModelViewSet):
    queryset = PayrollScheme.objects.all()
    serializer_class = PayrollSchemeSerializer


class TimeOffSchemeViewSet(viewsets.ModelViewSet):
    queryset = TimeOffScheme.objects.all()
    serializer_class = TimeOffSchemeSerializer


class OvertimeViewSet(viewsets.ModelViewSet):
    queryset = Overtime.objects.all()
    serializer_class = OvertimeSerializer


class OvertimeDtlViewSet(viewsets.ModelViewSet):
    queryset = OvertimeDtl.objects.all()
    serializer_class = OvertimeDtlSerializer


class TaxSetupViewSet(viewsets.ModelViewSet):
    queryset = TaxSetup.objects.all()
    serializer_class = TaxSetupSerializer


class TaxSetupDtlViewSet(viewsets.ModelViewSet):
    queryset = TaxSetupDtl.objects.all()
    serializer_class = TaxSetupDtlSerializer


class AbsentPatternViewSet(viewsets.ModelViewSet):
    queryset = AbsentPattern.objects.all()
    serializer_class = AbsentPatternSerializer


class AbsentPatternDtlViewSet(viewsets.ModelViewSet):
    queryset = AbsentPatternDtl.objects.all()
    serializer_class = AbsentPatternDtlSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class FieldOfStudyViewSet(viewsets.ModelViewSet):
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class CompanyCareerViewSet(viewsets.ModelViewSet):
    queryset = CompanyCareer.objects.all()
    serializer_class = CompanyCareerSerializer


class FamilyInfoViewSet(viewsets.ModelViewSet):
    queryset = FamilyInfo.objects.all()
    serializer_class = FamilyInfoSerializer


class EducationInfoViewSet(viewsets.ModelViewSet):
    queryset = EducationInfo.objects.all()
    serializer_class = EducationInfoSerializer


class CareerInfoViewSet(viewsets.ModelViewSet):
    queryset = CareerInfo.objects.all()
    serializer_class = CareerInfoSerializer


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicantListSerializer
        else:
            return ApplicantSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        else:
            return EmployeeSerializer


class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

