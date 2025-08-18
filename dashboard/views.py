import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import WorldBankData


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_gdp_data(request):
    """Fetch GDP data from World Bank API"""
    countries = request.GET.get('countries', 'US;CN;IN;DE;JP').split(';')
    start_year = request.GET.get('start_year', '2010')
    end_year = request.GET.get('end_year', '2022')
    
    data = []
    
    for country in countries:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/NY.GDP.MKTP.CD"
        params = {
            'date': f"{start_year}:{end_year}",
            'format': 'json',
            'per_page': 50
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                json_data = response.json()
                if len(json_data) > 1 and json_data[1]:
                    for item in json_data[1]:
                        if item['value']:
                            data.append({
                                'country': item['country']['value'],
                                'year': int(item['date']),
                                'value': float(item['value']),
                                'indicator': 'GDP (current US$)'
                            })
        except Exception as e:
            print(f"Error fetching data for {country}: {e}")
    
    return Response({'data': data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_population_data(request):
    """Fetch Population data from World Bank API"""
    countries = request.GET.get('countries', 'US;CN;IN;DE;JP').split(';')
    start_year = request.GET.get('start_year', '2010')
    end_year = request.GET.get('end_year', '2022')
    
    data = []
    
    for country in countries:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/SP.POP.TOTL"
        params = {
            'date': f"{start_year}:{end_year}",
            'format': 'json',
            'per_page': 50
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                json_data = response.json()
                if len(json_data) > 1 and json_data[1]:
                    for item in json_data[1]:
                        if item['value']:
                            data.append({
                                'country': item['country']['value'],
                                'year': int(item['date']),
                                'value': float(item['value']),
                                'indicator': 'Population, total'
                            })
        except Exception as e:
            print(f"Error fetching population data for {country}: {e}")
    
    return Response({'data': data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_co2_emissions_data(request):
    """Fetch CO2 emissions data from World Bank API"""
    countries = request.GET.get('countries', 'US;CN;IN;DE;JP').split(';')
    start_year = request.GET.get('start_year', '2010')
    end_year = request.GET.get('end_year', '2019')
    
    data = []
    
    for country in countries:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/EN.ATM.CO2E.KT"
        params = {
            'date': f"{start_year}:{end_year}",
            'format': 'json',
            'per_page': 50
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                json_data = response.json()
                if len(json_data) > 1 and json_data[1]:
                    for item in json_data[1]:
                        if item['value']:
                            data.append({
                                'country': item['country']['value'],
                                'year': int(item['date']),
                                'value': float(item['value']),
                                'indicator': 'CO2 emissions (kt)'
                            })
        except Exception as e:
            print(f"Error fetching CO2 data for {country}: {e}")
    
    return Response({'data': data})