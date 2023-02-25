import csv
from datetime import datetime

stops = []
distance = []
trips = {}

with open('1C - Westbound.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stops.append(row['stops'])
        distance.append(float(row['distance']))
        for key, value in row.items():
            if key.startswith('trip_'):
                if key not in trips:
                    trips[key] = []
                trips[key].append(datetime.strptime(value, '%H:%M'))

print('Stops:', stops)
print('Distance:', distance)
for key, value in trips.items():
    print(key + ':', value)