import csv
from datetime import datetime, timedelta
import time

class Bus:
    def __init__(self, route_id, direction, trip_id):
        bus_id = f"bus-{route_id}-{direction}-{trip_id}"
        self.bus_id = bus_id
        self.route_id = route_id
        self.direction = direction
        self.trip_id = trip_id
        self.location = None

    def deploy_to_trip(self, stops, trips):
        # Find the index of the first stop for this trip
        first_stop_index = -1
        for i, stop in enumerate(stops):
            if stop == self.trip_id:
                first_stop_index = i
                break

        # If the trip has already started, set the bus's location to the current stop
        if simulation_time.strftime('%H:%M') in trips[f'trip_{self.trip_id}']:
            self.location = stops[first_stop_index]

        # Otherwise, set the bus's location to the first stop
        else:
            self.location = stops[first_stop_index]
            print(f"A new {self.bus_id} has been deployed for trip {self.trip_id} on {self.route_id} - {direction_id} at {simulation_time.strftime('%H:%M')}")

    def move_to_stop(self, stop_name):
        print(f"{self.bus_id} is now at {stop_name} for trip {self.trip_id} on {self.route_id} - {direction_id} at {simulation_time.strftime('%H:%M')}")
        self.location = stop_name

    def complete_trip(self):
        print(f"Trip {self.trip_id} on {self.route_id} - {direction_id} has been completed by {self.bus_id} at {simulation_time.strftime('%H:%M')}")



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

                    # Check if a bus is already deployed for this trip
                    bus_deployed = False
                    for bus in direction_data.get('buses', []):
                        if bus.trip_id == trip_num.split('_')[1]:
                            bus_deployed = True
                            current_bus = bus
                            break

                    # If a bus is already deployed, move it to the current stop
                    if bus_deployed:
                        current_bus.move_to_stop(stop_name)

                        # Check if the bus has reached the final stop
                        if stop_index == len(direction_data['stops']) - 1:
                            current_bus.complete_trip()
                            direction_data['buses'].remove(current_bus)

                    # If no bus is deployed, create a new bus and deploy it to the trip
                    else:
                        # Generate a new unique bus id
                        new_bus = Bus(route_id=route_id,
                                    direction=direction_id,
                                    trip_id=trip_num.split('_')[1])
                        new_bus.deploy_to_trip(stops=direction_data['stops'], trips=direction_data['trips'])
                        direction_data.setdefault('buses', []).append(new_bus)

    # Pause the execution of the code for 1 second
    time.sleep(1)

    # Increment the simulation time by 1 minute
    simulation_time += timedelta(minutes=1)
