import LookUpLog
from Truck import Truck
import PrintColor


# Total
# Time complexity: O(n)
# Space complexity: O(1)

# Deliver function for truck in action
# Time complexity: O(n)
# Space complexity: O(1)
def deliver(truck):
    first_load = [1, 6, 13, 14, 15, 16, 19, 20, 21, 22, 29, 30, 31, 34, 37, 40]
    second_load = [2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 23, 24, 25, 26, 36, 38]
    third_load = [7, 8, 27, 28, 32, 33, 35, 39]

    if truck.truck_id == 'truck1':
        truck.loadPackages(first_load)
    if truck.truck_id == 'truck2':
        truck.loadPackages(second_load)
    if truck.truck_id == 'truck3':
        truck.loadPackages(third_load)

    PrintColor.prGreen("===============================================================")
    print(truck.truck_id, 'starts delivery at:', truck.start_time.time())
    PrintColor.prGreen("===============================================================")

    while truck.packages:
        truck.deliver_next_location()
    truck.back_to_hub()

    PrintColor.prGreen("===============================================================")
    print(truck.truck_id, 'Delivery route:', truck.delivery_route)
    print(truck.truck_id, 'Miles traveled:', round(truck.miles, 2))
    print(truck.truck_id, 'Time arrived at the Hub(in H:M format):', truck.current_time.hour, ':',
          truck.current_time.minute)
    PrintColor.prGreen("===============================================================")

    input("Press Enter to continue...")

    return True


# Start function to start simulation
# Time complexity: O(n)
# Space complexity: O(1)
def start():
    truck1 = Truck('truck1')
    truck2 = Truck('truck2')
    truck3 = Truck('truck3')

    deliver(truck1)
    truck2.start_time = truck1.current_time
    truck2.current_time = truck1.current_time

    deliver(truck2)
    truck3.start_time = truck2.current_time
    truck3.current_time = truck2.current_time

    deliver(truck3)
    total_miles_traveled = truck1.miles + truck2.miles + truck3.miles
    PrintColor.prGreen("===============================================================")
    print("All packages are delivered")
    print('Total miles traveled by all trucks:', round(total_miles_traveled, 2))
