# PART 1 - USER INPUT
city = input("Enter your city name:")
temp = float(input("Enter today's temperature in C:"))


# PART 2 - if STATEMENT
if temp> 35:
    print("Warning: It is very hot today!")


# PART 3 - if-elif-else
if temp > 35:
    print("Weather: Scorching Hot")
elif temp > 25:
    print("Weather: Warm and Sunny")
elif temp > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")


    # PART 4 - detetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))