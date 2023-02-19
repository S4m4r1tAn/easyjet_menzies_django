from django.urls import path
from . import views

urlpatterns = [
    path('flight-data/', views.get_flight_data, name='flight-data'),
]
