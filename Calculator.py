import tkinter as tk

def parse_time_input(time_entry):
    parts = time_entry.split(':')
    parts_int = [int(p) for p in parts]

    if len(parts_int) == 1:
        hours = 0
        minutes = 0
        seconds = parts_int
    elif len(parts_int) == 2:
        hours = 0
        minutes, seconds = parts_int
    elif len(parts_int) == 3:
        hours, minutes, seconds = parts_int
    else:
        result_label.config(text="Invalid Time Format")
        return None
    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes

def parse_pace_input(pace_entry):
    parts = pace_entry.split(':')
    parts_int = [int(p) for p in parts]

    if len(parts_int) == 1:
        minutes = 0
        seconds = parts_int[0]
    elif len(parts_int) == 2:
        minutes, seconds = parts_int
    else:
        result_label.config(text="Invalid Time Format")
        return None

    total_minutes_per_mile = minutes + seconds / 60
    return total_minutes_per_mile

def on_button_click():
    distance_entry_get = distance_entry.get()
    time_entry_get = time_entry.get()
    pace_entry_get = pace_entry.get()

    distance = float(distance_entry_get) if distance_entry_get else None
    time_min = parse_time_input(time_entry_get) if time_entry_get else None
    pace_min_per_mile = parse_pace_input(pace_entry_get) if pace_entry_get else None

    if distance is None and time_min is not None and pace_min_per_mile is not None:
        distance = time_min / pace_min_per_mile
        result_label.config(text=f"You ran {distance:.2f} miles.")

    elif time_min is None and distance is not None and pace_min_per_mile is not None:
        time_min = distance * pace_min_per_mile
        hours = int(time_min // 60)
        minutes = int(time_min % 60)
        seconds = int((time_min - int(time_min)) * 60)
        result_label.config(text=f"Your time was {hours:02}:{minutes:02}:{seconds:02}")

    elif pace_min_per_mile is None and distance is not None and time_min is not None:
        pace_min_per_mile = time_min / distance
        pace_minutes = int(pace_min_per_mile)
        pace_seconds = int((pace_min_per_mile - pace_minutes) * 60)
        result_label.config(text=f"Your pace was {pace_minutes}:{pace_seconds:02} per mile.")

    else:
        result_label.config(text="Please enter exactly two of the three values: distance, time, or pace.")

root = tk.Tk()
root.title("Running Calculator")
root.geometry("500x400")

tk.Label(root, text="Welcome to the Running Calculator!", font=("Times New Roman", 16), fg="black").pack()
tk.Label(root, text="For whatever metric you want to calculator, just leave it blank and fill in the other two.", 
         font=("Times New Roman", 9), pady=30).pack()

tk.Label(root, text="Enter distance (in miles): ").pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

tk.Label(root, text="Enter time (HH:MM:SS):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Enter pace (MM:SS per mile):").pack()
pace_entry = tk.Entry(root)
pace_entry.pack()
tk.Button(root, text="Enter", command=on_button_click).pack()
result_label = tk.Label(root, text="", font=("Times New Roman", 9))
result_label.pack()
root.mainloop()