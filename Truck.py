import LookUpLog
import PrintColor
from CSVreader import get_distance_data, get_package_location_name_data, package_input_data_hashmap
from Algorithms import get_all_distance_list, search_for_match, cal_each_trip_time
import datetime

distance_data = get_distance_data()
package_location_name_data = get_package_location_name_data()


# Total
# Time complexity: O(n)
# Space complexity: O(n)

class Truck:

    # initializing data
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self, truck_id, start_time=datetime.datetime(2023, 7, 1, 8, 00, 00)):
        self.truck_id = truck_id
        self.miles = 0
        self.currentLocation = '4001 South 700 East'
        self.previousLocation = ''
        self.packages = []
        self.package_id_address_pair = []
        self.delivery_route = []
        self.start_time = start_time
        self.current_time = self.start_time

    # Loading the packages to the truck
    # Time complexity: O(n)
    # Space complexity: O(1)
    def loadPackages(self, packageList):
        self.packages = packageList
        self.load_package_address_id_pair()
        return True

    # Looking for next closest location function
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def deliver_next_location(self):
        package_address_distance_list = []

        # Look for current location id with package data
        current_location_id = int(search_for_match(package_location_name_data, self.currentLocation)[0])
        all_distance_list = get_all_distance_list(current_location_id)

        # Pairing up the address id with package id
        self.load_package_address_id_pair()

        # Putting all the distance in miles into a list
        for i in self.package_id_address_pair:
            package_address_distance_list.append(float(all_distance_list[int(i[1])]))
        if not package_address_distance_list:
            return True

        # Using min function to look for the shortest distance to the current location
        shortest_distance = min(package_address_distance_list)

        # Using the shortest distance in miles to look for the location id of the closest location
        new_location_id = all_distance_list.index(shortest_distance)

        # Using the new location id to find the package id in the package_address_distance_list
        delivered_package_id = self.find_package_id(int(new_location_id))

        # Error handling for using the address id that does not belong to this truck
        while delivered_package_id is None:
            all_distance_list[new_location_id] = 'None'
            new_location_id = all_distance_list.index(shortest_distance)
            delivered_package_id = self.find_package_id(new_location_id)

        # Get the location name by looking up the package location list
        new_location = package_location_name_data[new_location_id][1]

        # Calculating the time require to the new destination
        time_taken = round(cal_each_trip_time(shortest_distance))

        # Updating truck information, name of the new location, distance traveled in miles,
        # current location id, id of delivered package, time taken in minutes

        self.update_truck_info(new_location, shortest_distance, current_location_id,
                               delivered_package_id, time_taken)

        # Updating information at 10:20 AM
        if self.current_time.hour == 10:
            if 15 < self.current_time.minute < 20:
                PrintColor.prYellow("==============================================")
                PrintColor.prYellow("10:20:00 New information of a package has come in for package #9 during delivery")

                self.update_package_data(9, 1, '410 S State St')
                self.update_package_data(9, 4, '84111')

                input("Press Enter to acknowledge...")
                PrintColor.prYellow('New information has been updated:')
                print(package_input_data_hashmap.get(9))
                PrintColor.prYellow("==============================================")
                input("Press Enter to continue...")

        print(self.current_time.time(), self.truck_id, 'package:',
              delivered_package_id, ' is delivered at', new_location)

        return True

    # Pairing address id and package id
    # Time complexity: O(n)
    # Space complexity: O(n)
    def load_package_address_id_pair(self):
        self.package_id_address_pair.clear()
        for i in self.packages:
            address_id = search_for_match(package_location_name_data, package_input_data_hashmap.get(i)[1])[0]
            self.package_id_address_pair.append([i, int(address_id)])

    # Find the package id that matches the address id
    # Time complexity: O(n)
    # Space complexity: O(1)
    def find_package_id(self, location_id):
        for i in self.package_id_address_pair:
            if i[1] == location_id:
                return i[0]

    # Find the package index number
    # Time complexity: O(n)
    # Space complexity: O(1)
    def find_package_index(self, package_id):
        for i in range(len(self.package_id_address_pair)):
            if self.package_id_address_pair[i][0] == package_id:
                return i

    # Function that takes the truck back to the hub
    # Time complexity: O(n)
    # Space complexity: O(1)
    def back_to_hub(self):

        current_location_id = int(search_for_match(package_location_name_data, self.currentLocation)[0])
        all_distance_list = get_all_distance_list(current_location_id)
        distance_to_hub = all_distance_list[0]
        time_taken = round(cal_each_trip_time(distance_to_hub))

        self.update_truck_info('4001 South 700 East', distance_to_hub, current_location_id, 0, time_taken)

        self.delivery_route.append(0)

        print(self.current_time.time(), self.truck_id, 'is back to the hub!')

        return self

    # Function for updating the truck information
    # Time complexity: O(n)
    # Space complexity: O(1)
    def update_truck_info(self, new_location, miles_traveled,
                          current_location_id, delivered_package_id, time_taken):

        self.previousLocation = self.currentLocation
        self.currentLocation = new_location

        self.miles += float(miles_traveled)

        self.delivery_route.append(current_location_id)

        if self.packages:
            self.packages.remove(delivered_package_id)

        # Start
        if self.current_time.hour == 8:
            if self.current_time.minute == 0:
                self.inject_data_into_time(self.current_time.hour, self.current_time.minute)

        if delivered_package_id == 0:

            for i in range(time_taken - 1):
                current_hour_w = self.current_time.hour
                current_minute_w = self.current_time.minute + (i + 1)

                if current_minute_w >= 60:
                    current_hour_w += 1
                    current_minute_w = 0 + (current_minute_w - 60)
                    self.inject_data_into_time(current_hour_w, current_minute_w)

                if current_minute_w <= 60:
                    self.inject_data_into_time(current_hour_w, current_minute_w)

            self.current_time = self.current_time + datetime.timedelta(minutes=time_taken)

            self.inject_data_into_time(self.current_time.hour, self.current_time.minute)

            return True

        # On the way
        self.update_package_data(delivered_package_id, 8, 'EN ROUTE')

        for i in range(time_taken - 1):
            current_hour_w = self.current_time.hour
            current_minute_w = self.current_time.minute + (i + 1)

            if current_minute_w >= 60:
                current_hour_w += 1
                current_minute_w = 0 + (current_minute_w - 60)
                self.inject_data_into_time(current_hour_w, current_minute_w)

            if current_minute_w <= 60:
                self.inject_data_into_time(current_hour_w, current_minute_w)

        # Arrive
        self.current_time = self.current_time + datetime.timedelta(minutes=time_taken)

        # Arrive
        display_time_after = self.current_time.time()
        self.update_package_data(delivered_package_id, 7, str(display_time_after))
        self.update_package_data(delivered_package_id, 8, 'Delivered')

        # Arrive
        self.inject_data_into_time(self.current_time.hour, self.current_time.minute)

        return True

    # injecting the data into the hashmap with time as a key
    # Time complexity: O(1)
    # Space complexity: O(1)
    def inject_data_into_time(self, current_time_hour, current_time_minute):
        all_package = []
        time = str(current_time_hour) + str(current_time_minute)
        for i in range(1, 41):
            all_package.append(package_input_data_hashmap.get(i))
        LookUpLog.set_lookup_log(int(time), all_package)

    # Updating package data's hashmap
    # Time complexity: O(n)
    # Space complexity: O(1)
    def update_package_data(self, delivered_package_id, pos, value):
        update_values = []

        if package_input_data_hashmap.get(delivered_package_id) is None:
            print("Its NONE")

        for i in package_input_data_hashmap.get(delivered_package_id):
            update_values.append(i)
        update_values[pos] = value
        package_input_data_hashmap.update(str(delivered_package_id), update_values)
