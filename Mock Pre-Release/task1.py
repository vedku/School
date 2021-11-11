import time
days = ["monday, tuesday, wednesday, thursday, friday, saturday, sunday"]
hour_of_arrival = []
frequent_parking_number = []
day = input("What day is it?:")
while day not in days
    input("Invalid entry! What day is it?")
print("ONLY INPUT THE HOUR OF ARRIVAL, EXCLUDE MINUTES. FOR EXAMPLE 15:45 becomes 15. USE 24 hour time")
time.sleep(3)
hour_of_arrival = int(input("What time have you arrived at?:"))
frequent_parking_number = input("What is your frequent parking number? If you have one:")
