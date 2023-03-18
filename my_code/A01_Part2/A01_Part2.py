# ------------------------------------------
# IMPORTS
# ------------------------------------------
import os
import csv
from collections import defaultdict
from datetime import datetime


# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    """
    Parse a line of the CSV file and return a dictionary with relevant information about the trip.

    Args:
        line (str): The unprocessed line of text in the CSV file.

    Returns:
        dict: A dictionary with the following keys: 'start_time', 'stop_time', 'start_station_id',
            'start_station_name', 'stop_station_id', 'stop_station_name', 'bike_id'.
    """
    res = {}
    fields = line.strip().split(",")
    if len(fields) == 16:
        res["start_time"] = datetime.strptime(fields[0], "%Y/%m/%d %H:%M:%S")
        res["stop_time"] = datetime.strptime(fields[1], "%Y/%m/%d %H:%M:%S")
        res["start_station_id"] = int(fields[3])
        res["start_station_name"] = fields[4]
        res["stop_station_id"] = int(fields[7])
        res["stop_station_name"] = fields[8]
        res["bike_id"] = int(fields[11])
    return res


# ------------------------------------------
# FUNCTION parse_in
# ------------------------------------------
def parse_in(input_folder, BIKE_ID):
    """
    Parses the input CSV files in the given directory and returns a list of relevant trips along with the stations they start and stop at.

    Args:
        input_folder (str): The path to the directory containing input CSV files.
        BIKE_ID (int): The ID of the bike that we are interested in.

    Returns:
        tuple: A tuple containing two elements:
            1. A list of dictionaries containing information about the trips.
            2. A dictionary containing information about the stations, where the keys are the station IDs and the values are the station names.
    """
    trips = []
    stations = defaultdict(str)

    with os.scandir(input_folder) as filenames:
        for filename in filenames:
            if filename.is_file():
                with open(filename, "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        trip = process_line(",".join(row))
                        if trip["bike_id"] == BIKE_ID:
                            trips.append(trip)
                            stations[trip["start_station_id"]] = trip["start_station_name"]
                            stations[trip["stop_station_id"]] = trip["stop_station_name"]
    return trips, stations


# ------------------------------------------
# FUNCTION parse_out
# ------------------------------------------
def parse_out(output_file, trips, stations):
    """
    Write trip information to an output file in a specific format.

    Args:
        output_file (file): The output file to write the trip information to.
        trips (list): A list of dictionaries containing the trip information.
        stations (dict): A dictionary mapping station IDs to their names.

    Returns:
        count (int): Count file write iterations
    """
    count = 0
    for i in range(len(trips)-1):
        current_trip = trips[i]
        next_trip = trips[i+1]

        if current_trip["stop_station_id"] != next_trip["start_station_id"]:
            start_time = current_trip["stop_time"].strftime("%Y/%m/%d %H:%M:%S")
            start_station = stations[current_trip["stop_station_id"]]
            end_time = next_trip["start_time"].strftime("%Y/%m/%d %H:%M:%S")
            end_station = stations[next_trip["start_station_id"]]

            output = f"By_Truck\t({start_time}, {start_station}, {end_time}, {end_station})\n"
            output_file.write(output)
            count += 1
    return count


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_folder, output_file, BIKE_ID):
    trips, stations = parse_in(input_folder, BIKE_ID)
    count = parse_out(output_file, trips, stations)
    
    print("{} entries written to '{}'".format(count, output_file))


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    input_folder = "../../my_dataset/"
    output_file = "../../my_results/Student_Solutions/A01_Part2/result.txt"
    BIKE_ID = 35143
    with open(output_file, 'w') as f:
        my_main(input_folder, f, BIKE_ID)
