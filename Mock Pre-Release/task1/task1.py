import time
days = ["1", "2", "3", "4", "5", "6", "7"]
hour_of_arrival = []
hours = []
frequent_parking_number = []
print("The day of the week is represented by a number. For example, monday is 1. Accordingly answer the question")
time.sleep(3)
day = int(input("What day is it?:"))
print("ONLY INPUT THE HOUR OF ARRIVAL, EXCLUDE MINUTES. FOR EXAMPLE 15:45 becomes 15. USE 24 hour time")
time.sleep(3)
hour_of_arrival = int(input("What time have you arrived at?:"))
hours = int(input("How many hours did you park for?:"))
frequent_parking_number = int(input("What is your frequent parking number? If you have one:"))
