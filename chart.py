from datetime import datetime
from bokeh.plotting import figure, show, output_file
import re

def parse_file(file_path):
    timestamps = []
    bitrates = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for item in lines:
            timestamp = re.findall(r"Timestamp: (.+)",item)
            if timestamp:
                timestamp_group = timestamp[0]  # Access the first match from the list
                timestamps.append(datetime.strptime(timestamp_group, "%Y-%m-%d %H:%M:%S"))
            if "sender" in item:
                bitrate = re.findall(r"(\d+\.\d+|\d+) Mbits/sec", item)
                bitrate2 = re.findall(r"(\d+\.\d+|\d+) Kbits/sec", item)
                if bitrate:
                        bitrates.append(float(bitrate[0]))  # Access the first match
                elif bitrate2:
                        bitrates.append(float(bitrate2[0]) / 1000) 
    return timestamps, bitrates
file_path = "soal_chart_bokeh.txt"
timestamps, bitrates = parse_file(file_path)

output_file("chart.html")

p = figure(x_axis_type="datetime", 
   title="Sender Speed Over Time",width=1000,
   height=500, x_axis_label="Date Time",
   y_axis_label="Speed(Mbps)",)
p.line(timestamps, bitrates, line_width=3)
        
show(p)