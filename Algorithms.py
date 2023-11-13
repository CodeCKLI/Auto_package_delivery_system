from CSVreader import get_distance_data, get_package_location_name_data

# Retrieving data from CSVreader.py
distance_data = get_distance_data()
package_name_data = get_package_location_name_data()


# Total
# Time complexity: O(n^2)
# Space complexity: O(n)

# Calculates time taken to destination in minutes
# Time complexity: O(1)
# Space complexity: O(1)
def cal_each_trip_time(distance):
    time = (distance / 18) * 60
    return time


# Putting distance data related to the location in a list
# Time complexity: O(n)
# Space complexity: O(n)
def get_all_distance_list(location_id):
    all_distance = []
    for i in range(len(distance_data)):
        result = distance_data[i][location_id]
        if result == '':
            result = distance_data[location_id][i]
        all_distance.append(float(result))
    return all_distance


# Search for match in data
# Time complexity: O(n^2)
# Space complexity: O(n)
def search_for_match(data, target):
    for row in data:
        for item in row:
            if target in item:
                return row
    return None
