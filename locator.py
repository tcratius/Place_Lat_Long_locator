from geopy.geocoders import Nominatim
import csv


geolocator = Nominatim()

"""
Open CSV file for writing
"""
with open('new_loc2.csv', 'wb') as write_csvfile:
    file_writer = csv.writer(write_csvfile)

    """
    Open CSV file for reading
    Read each row in read_file
    Assign Nominatim geocode functions results of each row to location
    Write to file
    """
    new_list = []
    with open('loc_csv.csv', 'rb') as read_csvfile:
        read_file = csv.reader(read_csvfile)
        for row in read_file:
            location = geolocator.geocode(row, timeout=10)
            if location:
                new_list = row
                new_list.append(location.latitude)
                new_list.append(location.longitude)
                file_writer.writerow(new_list)
