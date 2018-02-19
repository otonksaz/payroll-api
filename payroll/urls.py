"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as tokenViews
from payroll.mainapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'companies', views.CompanyViewSet, base_name='company-view')
router.register(r'divisions', views.DivisionViewSet, base_name='division-view')
router.register(r'jobpositions', views.JobPositionViewSet, base_name='jobposition-view')
router.register(r'joblevels', views.JobLevelViewSet, base_name='joblevel-view')
router.register(r'payrollcomponents', views.PayrollComponentViewSet, base_name='payrollcomponent-view')
router.register(r'payrollcomponentdtls', views.PayrollComponentDtlViewSet, base_name='payrollcomponentdtl-view')
router.register(r'payrollschemes', views.PayrollSchemeViewSet, base_name='payrollscheme-view')
router.register(r'prorates', views.ProRateViewSet, base_name='prorate-view')
router.register(r'timeoffpolicies', views.TimeOffPolicyViewSet, base_name='timeoffpolicy-view')
router.register(r'timeoffschemes', views.TimeOffSchemeViewSet, base_name='timeoffscheme-view')
router.register(r'overtimes', views.OvertimeViewSet, base_name='overtime-view')
router.register(r'overtimedtls', views.OvertimeDtlViewSet, base_name='Overtimedtl-view')
router.register(r'taxsetups', views.TaxSetupViewSet, base_name='taxsetup-view')
router.register(r'taxsetupdtls', views.TaxSetupDtlViewSet, base_name='taxsetupdtl-view')
router.register(r'absentpatterns', views.AbsentPatternViewSet, base_name='absentpattern-view')
router.register(r'absentpatterndtls', views.AbsentPatternDtlViewSet, base_name='absentpatterndtl-view')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', tokenViews.obtain_auth_token),
]
