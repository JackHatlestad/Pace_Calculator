
def get_float_input(Prompt):
    value = input(Prompt)
    return float(value) if value else None

def parse_time_input(Time):
    parts = Time.split(':')
    
    try:
        parts_int = [int(p) for p in parts]
    except ValueError:
        print("Invalid input, please enter numbers separated by ':'")
        return None
    
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
    
    try:
        parts_int = [int(p) for p in parts]
    except ValueError:
        print("Invalid input, please enter numbers separated by ':'")
        return None
    
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

Distance = get_float_input("Enter distance (in miles): ")
Time = input("How long did it take in HH:MM:SS?")
Pace = input("What was your pace? MM:SS")

print(get_float_input(Distance))
5



Time_Minutes = float(parse_time_input(Time))

Pace = Time_Minutes / Distance
print(Pace)
