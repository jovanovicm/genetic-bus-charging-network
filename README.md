## Creating a Genetic Algorithm to optimize bus charging schedules for Windsor Transit

#### What has to be done with the current scope:
- Create a system that can track multiple trips and trip times in the `H:MM` format and notify us in the console if
a bus has arrived at a bus station. Once a trip is complete, the simulation should no longer scrape its datetime values
to notify if a bus has arrived. 

- Integrate a bus class that can be deployed on a route automatically and the notification system should notify when a
specific bus has arrived. 

- Buses should be able to transfer between trips once they are completed between 2 different csv files. Csv files should
be paired with a WEST/EAST and NORTH/SOUTH pairing. If a bus completes a trip, there should be a wait time which will
later be replaced with a charging time, and then the bus should check the current time, and take over the trip closest to it.

```Bus finishes trip_1 at 7:28
Has an idle time (charging time) for 45 minutes
Current time is 8:13
trip_14 starts at 8:15 from the terminal the bus is at
Instead of creating a new bus for trip_14, use the existing bus to take over the trip.
```



