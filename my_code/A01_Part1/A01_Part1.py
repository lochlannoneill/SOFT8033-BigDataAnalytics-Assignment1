#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# This program retrieves the unique start and stop station names from the CSV files in the input folder and writes them
# along with their respective counts to a tab-separated output file.
#
# The program provides three functions:
# (1) process_line(line): Parses a line of the CSV file and returns a dictionary.
# (2) get_stations(input_folder): Gets the unique start and stop station names from the CSV files in the input folder.
# (3) write_stations(output_file, starts, stops, names): Writes list of stations and their respective counts to file.
#
# --------------------------------------------------------


# ------------------------------------------
# IMPORTS
# ------------------------------------------
import os
import codecs
import csv
from collections import defaultdict


# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    """
    Parse a line of the CSV file and return a tuple of start and stop station names.

    Args:
        line (str): The unprocessed line.

    Returns:
        tuple: A tuple of two strings, representing the start and stop station names, respectively.
    """
    res = {}
    fields = line.strip().split(",")
    if (len(fields) == 16):
        # res['start_time'] = fields[0]
        # res['stop_time'] = fields[1]
        # res['trip_duration'] = int(fields[2])
        # res['start_station_id'] = int(fields[3])
        res['start_station_name'] = fields[4]
        # res['start_station_latitude'] = float(fields[5])
        # res['start_station_longitude'] = float(fields[6])
        # res['stop_station_id'] = int(fields[7])
        res['stop_station_name'] = fields[8]
        # res['stop_station_latitude'] = float(fields[9])
        # res['stop_station_longitude'] = float(fields[10])
        # res['bike_id'] = int(fields[11])
        # res['user_type'] = fields[12]
        # res['birth_year'] = int(fields[13])
        # res['gender'] = int(fields[14])
        # res['trip_id'] = int(fields[15])
    return res['start_station_name'], res['stop_station_name']


# ------------------------------------------
# FUNCTION process_csv
# ------------------------------------------
def get_stations(input_folder):
    """
    Returns unique start and stop station names from the CSV files in the input folder, along with the count of each
    occurrence.

    Args:
        input_folder (str): The path to the input folder containing the CSV files.

    Returns:
        tuple: A tuple of three items. The first item is a sorted list of unique station names, including all stations
        that appear as either a start or stop station. The second item is a dictionary containing the count of each unique
        start station name. The third item is a dictionary containing the count of each unique stop station name.
    """
    starts = defaultdict(int)  # Initialise value with 0, automatically creates default value for nonexistant key
    stops = defaultdict(int)
    with os.scandir(input_folder) as filenames:  # os.scandir() is a generator => better performance than os.listdir()
        for filename in filenames:
            if filename.is_file():
                with open(filename, 'r') as file:
                    for line in file:
                        start_name, stop_name = process_line(line)
                        starts[start_name] += 1
                        stops[stop_name] += 1
    all_names = sorted(set(starts.keys()) | set(stops.keys()))

    return starts, stops, all_names


# ------------------------------------------
# FUNCTION write_output
# ------------------------------------------
def write_stations(output_file, starts, stops, names):
    """
    Writes list of stations and their respective counts to file.

    Args:
        output_file (str): The name of the output file.
        names (list): A list of unique station names to include in the output file.
        starts (defaultdict): A dictionary containing the count of each unique start station name.
        stops (defaultdict): A dictionary containing the count of each unique stop station name.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        for name in names:
            start_count = starts.get(name, 0)
            stop_count = stops.get(name, 0)
            file.write(f"{name}\t({start_count}, {stop_count})\n")



# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_folder, output_file):
    starts, stops, names = get_stations(input_folder)
    print(len(starts), 'starts => ', dict(list(starts.items())[-3:]))  # 796
    print(len(stops), 'stops => ', dict(list(stops.items())[-3:]))  # 799
    print(len(names), 'names => ', names[-3:])

    write_stations(output_file, starts, stops, names)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    input_folder = "../../my_dataset/"
    output_file = "../../my_results/Student_Solutions/A01_Part1/result.txt"

    my_main(input_folder, output_file)
