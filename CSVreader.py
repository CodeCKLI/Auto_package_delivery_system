import csv

from HashMapImpl import HashMap

# Total
# Time complexity: O(n)
# Space complexity: O(n)

# Read data from the csv file
# Time complexity: O(n)
# Space complexity: O(n)
with open('WGUPS_Distance_Table_csv.csv') as distance_file:
    distance_csv = csv.reader(distance_file, delimiter=',')
    distance_data = list(distance_csv)

# Read data from the csv file
# Time complexity: O(n)
# Space complexity: O(n)
with open('WGUPS_Package_File_Names_csv.csv') as package_name_file:
    package_name_csv = csv.reader(package_name_file, delimiter=',')
    package_name_data = list(package_name_csv)

# Read data from the csv file
# Time complexity: O(n)
# Space complexity: O(n)
with open('WGUPS_Package_File_clean_csv.csv') as input_file:
    readData = csv.reader(input_file, delimiter=',')
    package_input_data_hashmap = HashMap()

    # Assigning data into variables
    for row in readData:
        package_id = row[0]
        address = row[1]
        deadline = row[2]
        city = row[3]
        zipcode = row[4]
        mass = row[5]
        note = row[6]
        delivery_time = ''
        delivery_status = 'At hub'

        datavalues = [package_id, address, deadline, city, zipcode, mass, note, delivery_time, delivery_status]

        # Inserting the values to hashmap
        key = package_id
        value = datavalues
        package_input_data_hashmap.insert(key, value)


# Distance data getter
def get_distance_data():
    return distance_data


# Package hashmap getter
def get_package_location_name_data():
    return package_name_data

