import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape the airport community app
url = 'https://www.example.com/airport-community-app'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data
table = soup.find('table', {'class': 'flights-table'})
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    flight = cols[0].text.strip()
    origin = cols[1].text.strip()
    destination = cols[2].text.strip()
    status = cols[3].text.strip()
    
    # Add filter for airline and airport codes
    if flight.startswith('Easyjet') and (origin == 'LTN' or destination == 'LTN'):
        data.append([flight, origin, destination, status])

# Scrape flightradar24
url = 'https://www.example.com/flightradar24'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data
table = soup.find('table', {'class': 'flights-table'})
rows = table.find_all('tr')

for row in rows[1:]:
    cols = row.find_all('td')
    flight = cols[0].text.strip()
    origin = cols[1].text.strip()
    destination = cols[2].text.strip()
    status = cols[3].text.strip()
    
    # Add filter for airline and airport codes
    if flight.startswith('U2') and (origin == 'LTN' or destination == 'LTN'):
        data.append([flight, origin, destination, status])

# Store the data in a Pandas DataFrame
df = pd.DataFrame(data, columns=['Flight', 'Origin', 'Destination', 'Status'])

# Filter the data to show only the flights going to the hangar for repair
hangar_flights = df[df['Status'] == 'Hangar']

# Generate the report
report = hangar_flights.to_html(index=False)

# Write the report to a file
with open('hangar_flights_report.html', 'w') as f:
    f.write(report)
