import os
import csv
from collections import defaultdict
from datetime import datetime

def process_line(line):
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


def parse_in(input_folder, BIKE_ID):
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


def parse_out(output_file, trips, stations):
    for i in range(len(trips)-1):
        current_trip = trips[i]
        next_trip = trips[i+1]

        if current_trip["stop_station_id"] != next_trip["start_station_id"]:
            move_start_time = current_trip["stop_time"]
            move_start_station = stations[current_trip["stop_station_id"]]
            move_end_time = next_trip["start_time"]
            move_end_station = stations[next_trip["start_station_id"]]

            output = "By_Truck\t({}, {}, {}, {})\n".format(
                move_start_time.strftime("%Y/%m/%d %H:%M:%S"), move_start_station,
                move_end_time.strftime("%Y/%m/%d %H:%M:%S"), move_end_station)
            output_file.write(output)

    output_file.close()


def my_main(input_folder, output_file, BIKE_ID):
    trips, stations = parse_in(input_folder, BIKE_ID)
    parse_out(output_file, trips, stations)


if __name__ == '__main__':
    input_folder = "../../my_dataset/"
    output_file = "../../my_results/Student_Solutions/A01_Part2/result.txt"
    BIKE_ID = 35143
    with open(output_file, 'w') as f:
        my_main(input_folder, f, BIKE_ID)
