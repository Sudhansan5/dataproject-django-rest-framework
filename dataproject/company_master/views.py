from django.shortcuts import render
from company_master.models import CompanyData
from django.db.models import Case, When, Value, CharField, Count
from company_master.serializers import AuthSerializer, RegistrationSerializer,\
    TopRegSerializer, PbaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.


def home_view(request):
    '''
    View for home page
    '''
    return render(request, "home.html")


def problem_one_view(request):
    '''
    View for problem one
    '''
    return render(request, "problem_one.html")


def problem_two_view(request):
    '''
    View for problem two
    '''
    return render(request, "problem_two.html")


def problem_three_view(request):
    '''
    View for problem three
    '''
    return render(request, "problem_three.html")


def problem_four_view(request):
    '''
    View for problem 4
    '''
    return render(request, "problem_four.html")


@api_view(['POST'])
def plot_one(request):
    '''
    This function returns JSON data for Plot 1.
    '''

    if request.method == 'POST':
        data = json.loads(request.body)
        year = int(data["year"])
        endyear = int(data["range"])+year
        company_type = data["company_type"]

        query = CompanyData.objects.filter(
            DATE_OF_REGISTRATION__year__range=(year, endyear),
            COMPANY_CLASS=company_type
            ).annotate(intervals=Case(
                When(AUTHORIZED_CAP__lte=100000, then=Value('<=1L')),
                When(AUTHORIZED_CAP__gte=100000,
                     AUTHORIZED_CAP__lte=1000000,
                     then=Value('1L to 10L')),
                When(AUTHORIZED_CAP__gte=1000000,
                     AUTHORIZED_CAP__lte=100000000,
                     then=Value('10L to 1Cr')),
                When(AUTHORIZED_CAP__gte=10000000,
                     AUTHORIZED_CAP__lte=1000000000,
                     then=Value('1Cr to 10Cr')),
                default=Value('>10Cr'),
                output_field=CharField(),
            )
        ).values('intervals').annotate(count=Count('intervals'))

    serializer = AuthSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def plot_two(request):
    '''
    This function returns JSON data for Plot 2.
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        start_year = int(data["start_year"])
        end_year = int(data["end_year"])
        pba = data["pba"]
        query = CompanyData.objects.filter(
            DATE_OF_REGISTRATION__year__range=(start_year, end_year),
            BUSINESS_ACTIVITY=pba
        ).values('DATE_OF_REGISTRATION__year').\
            annotate(count=Count('DATE_OF_REGISTRATION__year'))
    serializer = RegistrationSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def plot_three(request):
    '''
    This function returns JSON data for Plot 3.
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        year = int(data["year"])
        month = int(data["month"])
        top = int(data["top"])
        query = CompanyData.objects.filter(
            DATE_OF_REGISTRATION__year=year,
            DATE_OF_REGISTRATION__month__lte=month
            ).values(
                'BUSINESS_ACTIVITY'
                ).annotate(count=Count('BUSINESS_ACTIVITY'))\
            .order_by('-count')[:top]

    serializer = TopRegSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def plot_four(request):
    '''
    This function returns JSON data for Plot 4.
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        start_year = int(data["start_year"])
        end_year = int(data["range"]) + start_year
        pba = data["pba"]
        query = CompanyData.objects.filter(
            DATE_OF_REGISTRATION__year__range=(start_year, end_year),
            BUSINESS_ACTIVITY__in=pba
            ).values(
                 'DATE_OF_REGISTRATION__year', 'BUSINESS_ACTIVITY'
                ).annotate(count=Count('DATE_OF_REGISTRATION__year'))

    serializer = PbaSerializer(query, many=True)
    return Response(serializer.data)
