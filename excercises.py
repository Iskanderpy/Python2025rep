import math

width = 17
height = 12.0
delimiter = '.'

print(width / 2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5)
print(delimiter * 5)

# Exercise 2.3
radius = 5
volume = (4 / 3) * math.pi * (radius ** 3)
print(volume)

cover_price = 24.95
discount = 0.40
discounted_price = cover_price * (1 - discount)
total_cost = (discounted_price * 60) + 3 + (59 * 0.75)
print(total_cost)

start_time_minutes = 6 * 60 + 52
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12
total_run_seconds = (easy_pace * 2) + (tempo_pace * 3)
end_time_minutes = start_time_minutes + total_run_seconds // 60
end_seconds = total_run_seconds % 60
end_hour = end_time_minutes // 60
end_minute = end_time_minutes % 60
print(end_hour, ":", end_minute, ":", end_seconds)
