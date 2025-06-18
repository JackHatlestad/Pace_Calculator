import pandas as pd 
from datetime import datetime
import os
import tkinter as tk

def get_float_input(prompt):
    value = input(prompt)
    return float(value) if value else None

def parse_time_input(time_str):
    parts = time_str.split(':')
    parts_int = [int(p) for p in parts]

    if len(parts_int) == 1:
        hours = 0
        minutes = 0
        seconds = parts_int[0]
    elif len(parts_int) == 2:
        hours = 0
        minutes, seconds = parts_int
    elif len(parts_int) == 3:
        hours, minutes, seconds = parts_int
    else:
        print("Invalid time format")
        return None

    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes

def parse_pace_input(pace_str):
    parts = pace_str.split(':')
    parts_int = [int(p) for p in parts]

    if len(parts_int) == 1:
        minutes = 0
        seconds = parts_int[0]
    elif len(parts_int) == 2:
        minutes, seconds = parts_int
    else:
        print("Invalid pace format")
        return None

    total_minutes_per_mile = minutes + seconds / 60
    return total_minutes_per_mile

root = tk.Tk()
root.title("Welcome to the Pace Calculator")
root.mainloop()

# print("Welcome to the Pace Calculator")
distance = get_float_input("Enter distance (in miles), or leave blank: ")
time_str = input("Enter time (HH:MM:SS), or leave blank: ")
pace_str = input("Enter pace (MM:SS per mile), or leave blank: ")

time_min = parse_time_input(time_str) if time_str else None
pace_min_per_mile = parse_pace_input(pace_str) if pace_str else None

if distance is None and time_min is not None and pace_min_per_mile is not None:
    # Calculate distance
    distance = time_min / pace_min_per_mile
    distance = round(distance,2)
    print(f"You ran {distance:.2f} miles.")

elif time_min is None and distance is not None and pace_min_per_mile is not None:
    # Calculate time
    time_min = distance * pace_min_per_mile
    hours = int(time_min // 60)
    minutes = int(time_min % 60)
    seconds = int((time_min - int(time_min)) * 60)
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(f"Your time was {hours:02}:{minutes:02}:{seconds:02}")

elif pace_min_per_mile is None and distance is not None and time_min is not None:
    # Calculate pace
    pace_min_per_mile = time_min / distance
    pace_minutes = int(pace_min_per_mile)
    pace_seconds = int((pace_min_per_mile - pace_minutes) * 60)
    pace_str = f"{pace_minutes}:{pace_seconds:02}"
    print(f"Your pace was {pace_minutes}:{pace_seconds:02} per mile.")

else:
    print("Please enter exactly two of the three values: distance, time, or pace.")

running_stats = pd.DataFrame(columns=["Date", "Time", "Distance", "Pace"])


today = datetime.today()
formatted_date = today.strftime("%m/%d/%Y")

# New row as a DataFrame
new_row = pd.DataFrame([{
    "Date": formatted_date,
    "Time": time_str,
    "Distance": distance,
    "Pace": pace_str
}])

# Add the new row
running_stats = pd.concat([running_stats, new_row], ignore_index=True)

if not os.path.exists("running_data.xlsx"):
    running_stats.to_excel("running_data.xlsx", index=False)  # First time: write with header
else:
    running_stats.to_excel("running_data.xlsx", mode="a", header=False, index=False)  # Append without header


