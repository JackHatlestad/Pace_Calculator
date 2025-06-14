
def get_float_input(Prompt):
    value = input(Prompt)
    return float(value) if value else None

def parse_time_input(Time):
    parts = Time.split(':')
    parts_int = [int(p) for p in parts]
    
    if len(parts_int) == 1:
        hours = 0
        minutes = 0
        seconds = parts_int[0]
    elif len(parts_int) == 2:
        hours = 0
        minutes = parts_int[0]
        seconds = parts_int[1]
    elif len(parts_int) == 3:
        hours, minutes, seconds = parts_int
    else:
        print("Invalid time format")
        return None
    
    hours_minutes = hours * 60
    seconds_minutes = seconds / 60

    minutes_total = minutes + hours_minutes + seconds_minutes
    
    return float(minutes_total) if minutes_total else None

def parse_pace_input(Pace):
    parts = Pace.split(':')
    
    parts_int = [int(p) for p in parts]
    
    if len(parts_int) == 1:
        minutes = 0
        seconds = parts_int[0]
    elif len(parts_int) == 2:
        minutes = parts_int[0]
        seconds = parts_int[1]
    else:
        print("Invalid time format")
        return None
    
    minutes = minutes + (seconds/60) 
    mph = 60 / minutes 
    return float(mph) if mph else None

print("Welcome to the Pace Calculator")
Distance = get_float_input("Enter distance (in miles): ")
Time = input("How long did it take in HH:MM:SS?")
Pace = input("What was your pace? MM:SS")

if get_float_input(Distance) is None:
    minutes = float(parse_time_input(Time) / 60)
    distance_result = round(float(parse_pace_input(Pace) * minutes), 2)
    print("You ran ", distance_result, " miles")
elif parse_time_input(Time) is None:
    time_hours = float(get_float_input(Distance) / parse_pace_input(Pace))
    time_minutes = time_hours * 60
    print(time_minutes)



Time_Minutes = float(parse_time_input(Time))

Pace = Time_Minutes / Distance

