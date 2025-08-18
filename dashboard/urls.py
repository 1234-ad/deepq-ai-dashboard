from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/gdp-data/', views.get_gdp_data, name='gdp_data'),
    path('api/population-data/', views.get_population_data, name='population_data'),
    path('api/co2-data/', views.get_co2_emissions_data, name='co2_data'),
]