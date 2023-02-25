import csv
from datetime import datetime, timedelta
import time

stops = []
distance = []
trips = {}

# Formatting data using CSV
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

#print('Stops:', stops)
#print('Distance:', distance)
#for key, value in trips.items():
#    print(key + ':', value)

# Set the initial simulation time
simulation_time = datetime.strptime('05:15', '%H:%M')

# Loop through each minute in the simulation time
while True:
    # Print the current simulation time
    print(f"Simulation time: {simulation_time.strftime('%H:%M')}")

    # Check if the current simulation time matches any of the trip times
    for trip_num, trip_times in trips.items():
        if simulation_time in trip_times:
            # Get the index of the stop corresponding to the current trip and simulation time
            stop_index = trip_times.index(simulation_time)
            stop_name = stops[stop_index]

            # Print a message indicating that a bus has arrived at the stop for the trip
            print(f"A bus has arrived at {stop_name} for trip {trip_num.split('_')[1]} at {simulation_time.strftime('%H:%M')}")

    # Increment the simulation time by 1 minute
    simulation_time += timedelta(minutes=1)

    # Pause the execution of the code for 1 second
    time.sleep(1)