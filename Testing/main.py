import csv
import time

#1C 21km

class Bus:
    def __init__(self, type, bus_number, battery_capacity = None, aecr_passenger = None, aecr_deadhead = None):
        self.type = type
        self.bus_number = bus_number
        self.battery_capacity = battery_capacity
        self.aecr_passenger = aecr_passenger
        self.aecr_deadhead = aecr_deadhead
        self.current_location = None

        if type == "type1":
            self.battery_capacity = 204 #kWh
            self.aecr_passenger = 1.2 #average energy consumption rate kWh/km with passengers
            self.aecr_deadhead = 1.1 #average energy consumption rate kWh/km deadheading

        if type == "type2":
            self.battery_capacity = 120 #kWh
            self.aecr_passenger = 1.0 #average energy consumption rate kWh/km with passengers
            self.aecr_deadhead = 0.9 #average energy consumption rate kWh/km deadheading

    def __repr__(self):
        return f"Bus {self.bus_number} || Location: {self.current_location} Battery capacity: {self.battery_capacity}kWh"

class Route:
    def __init__(self, stops):
        self.stops = stops
        self.timetable = {} # {stop_name: [departure_time_1, departure_time_2, ...]}

    def add_timetable(self, stop_name, departure_times):
        self.timetable[stop_name] = departure_times

     

