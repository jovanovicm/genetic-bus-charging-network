import csv
from datetime import datetime, timedelta
import time

# Create a dictionary to hold the stops, distances, and trips for each route
routes = {}

# Loop through each CSV file
for filename in ['1C - Westbound.csv', '1C - Eastbound.csv']:
    # Extract the route identification and direction from the filename
    route_id, direction = filename.split(' - ')
    direction = direction.split('.')[0].lower()

    # Create a new dictionary for this route if it doesn't already exist
    if route_id not in routes:
        routes[route_id] = {}

    # Create the lists for the stops, distances, and trips for this direction
    stops = []
    distance = []
    trips = {}

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stops.append(row['stops'])
            distance.append(float(row['distance']))
            for key, value in row.items():
                if key.startswith('trip_'):
                    if key not in trips:
                        trips[key] = []
                    trips[key].append(datetime.strptime(value, '%H:%M'))

    # Add the lists for this direction to the dictionary for this route
    routes[route_id][direction] = {
        'stops': stops,
        'distance': distance,
        'trips': trips
    }

# Set the initial simulation time
simulation_time = datetime.strptime('5:15', '%H:%M')

# Loop through each minute in the simulation time
while True:
    # Print the current simulation time
    print(f"Simulation time: {simulation_time.strftime('%H:%M')}")

    # Loop through each route
    for route_id, route_data in routes.items():
        # Loop through each direction for this route
        for direction_id, direction_data in route_data.items():
            # Check if the current simulation time matches any of the trip times for this direction
            for trip_num, trip_times in direction_data['trips'].items():
                if simulation_time in trip_times:
                    # Get the index of the stop corresponding to the current trip and simulation time
                    stop_index = trip_times.index(simulation_time)
                    stop_name = direction_data['stops'][stop_index]

                    # Print a message indicating that a bus has arrived at the stop for the trip
                    print(f"A bus has arrived at {stop_name} for trip {trip_num.split('_')[1]} on {route_id} - {direction_id} at {simulation_time.strftime('%H:%M')}")

                    # Check if the bus has reached the final stop
                    if stop_index == len(direction_data['stops']) - 1:
                        print(f"Trip {trip_num.split('_')[1]} on {route_id} - {direction_id} has been completed at {simulation_time.strftime('%H:%M')}")

    # Increment the simulation time by 1 minute
    simulation_time += timedelta(minutes=1)

    # Pause the execution of the code for 1 second
    time.sleep(1)
