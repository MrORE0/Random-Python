race_length = 10
time_minutes = 42
time_seconds = 42

total_seconds = (time_minutes * 60) + time_seconds
total_miles = race_length / 1.61

average_time = total_seconds / total_miles
average_seconds = round((average_time % 60) , 2)
average_minutes = average_time // 60
average_speed = round(total_miles / (total_seconds / 3600) , 2)

print("Total seconds: ", total_seconds)
print("Miles: ", total_miles)
print("My average time per mile was: %.1f m %.2f s" % (average_minutes, average_seconds))
print("speed (mph): ", average_speed)
