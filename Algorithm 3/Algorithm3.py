# Bryant Martinez
# Bryantmartinez322@csu.fullerton.edu

# Convert time string (HH:MM) to total minutes since midnight
def time_to_minutes(time_string):
    hours, minutes = map(int, time_string.split(':')) # Splits the time string into hours and minutes.
    return hours * 60 + minutes # Returns the total minutes

# Convert total minutes since midnight back to time string (HH:MM)
def minutes_to_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f'{hours:02}:{minutes:02}' # returns in correct format of (HH:MM)

# Calculate available times within a person's working period
def get_free_times(working_period, busy_schedule, min_duration):
    start, end = map(time_to_minutes, working_period)
    free_times, current = [], start


# Converts the given busy_schedule into total minutes
    for busy in busy_schedule:
        busy_start, busy_end = map(time_to_minutes, busy)

        # If there is a gap between current time and the next busy period that is longer than the minimum duration
        if current < busy_start and (busy_start - current) >= min_duration:
            free_times.append([minutes_to_time(current), minutes_to_time(busy_start)])
        
        # Moves current time to the end of the busy period
        current = max(current, busy_end)

    # Checks to see if there's free time until the working period ends
    if current < end and (end - current) >= min_duration:
        free_times.append([minutes_to_time(current), minutes_to_time(end)])

    return free_times

# Searches for the common free slots among all schedules
def common_free_times(schedules, working_periods, min_duration):


    # Finds each person's free slot
    all_free_times = [get_free_times(working_periods[i], schedules[i], min_duration) for i in range(len(schedules))]
    common_times = all_free_times[0]

    # Compare each person's free time slots and find overlaps
    for member_times in all_free_times[1:]:
        temp_common = []
        for slot1 in common_times:
            for slot2 in member_times:

                # Find the overlap between two free time slots
                start_common = max(time_to_minutes(slot1[0]), time_to_minutes(slot2[0]))
                end_common = min(time_to_minutes(slot1[1]), time_to_minutes(slot2[1]))

                # Checks if overlap is long enough
                if (end_common - start_common) >= min_duration:
                    temp_common.append([minutes_to_time(start_common), minutes_to_time(end_common)])
        common_times = temp_common

    return common_times

# Sample input from PDF file
person1_schedule = [['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_working_hours = ['9:00', '19:00']
person2_schedule = [['9:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_working_hours = ['9:00', '18:30']
duration = 30  # Minimum time for meeting in minutes

# Calculate available meeting times
schedules = [person1_schedule, person2_schedule]
working_periods = [person1_working_hours, person2_working_hours]
available_slots = common_free_times(schedules, working_periods, duration)

print(available_slots)  # This will print the result

