# Installing FlightRadarAPI:

# Basic Usage:
from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()
# Getting airports list:
airports = fr_api.get_airports()
# Getting airlines list:
airlines = fr_api.get_airlines()
# Getting flights list:
flights = fr_api.get_flights()
# zones = fr_api.get_zones()
zones = fr_api.get_zones()
# You can also get more information about a specific flight such as: 
# aircraft images, estimated time, trail, etc.
details = fr_api.get_flight_details(flights.id)
flights.set_flight_details(details)
print(f' Flying to', flights.destination_airport_name)

# Filtering flights and airports:
# Getting flights by airline:
airline_icao = "EASYJET"
thy_flights = fr_api.get_flights(airline = airline_icao)
# Getting flights by bounds:
bounds = fr_api.get_bounds(zones)
flights = fr_api.get_flights(bound = bounds)
# Getting airport by ICAO or IATA:
airport_icao = "LTN"
luton_airport = fr_api.get_airport(airport_icao)
# Getting and configuring Real-time Flight Tracker parameters:
params = fr_api.get_real_time_flight_tracker_config()
new_config = {'param1': value1, 'param2': value2, ...}
fr_api.set_real_time_flight_tracker_config(**new_config)
