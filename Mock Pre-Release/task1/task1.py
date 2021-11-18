#variables
days = [1,2,3,4,5,6,7]
hour_of_arrival = []
hours_parked = []
frequent_parking_number = []
timings = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
price = 0
#questions
print("The day of the week is represented by a number. For example, monday is 1. Accordingly answer the question using numbers ranging from 1 to 7")
day = int(input("What day is it?:"))
print("ONLY INPUT THE HOUR OF ARRIVAL, EXCLUDE MINUTES. FOR EXAMPLE 15:45 becomes 15. USE 24 hour time")
hour_of_arrival = int(input("What time have you arrived at?:"))

#validation for hours parked in a day
hours_parked = int(input("How many hours did you park for?:"))
while day ==1 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Monday. \nHow many hours did you park for?:"))
while day ==2 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Tuesday. \nHow many hours did you park for?:"))
while day ==3 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Wednesday. \nHow many hours did you park for?:"))
while day ==4 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Thursday. \nHow many hours did you park for?:"))
while day ==5 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Friday. \nHow many hours did you park for?:"))
while day ==6 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >4:
    hours_parked = int(input("You can't park for more than two hours on a Saturday. \nHow many hours did you park for?:"))
while day ==7 and  hour_of_arrival in  [8, 9, 10, 11, 12, 13, 14, 15] and hours_parked >8:
    hours_parked = int(input("You can't park for more than eight hours on a Sunday. \nHow many hours did you park for?:"))

#parking number
frequent_parking_number = input("Input your frequent parking number:")
num1 = int(frequent_parking_number[0])
num2 = int(frequent_parking_number[1])
num3 = int(frequent_parking_number[2])
num4 = int(frequent_parking_number[3])
x1 = (num1*5)
x2 = (num2*4)
x3 = (num3*3)
x4 = (num4*2)
full_numbers = (x1+x2+x3+x4)
modulo = full_numbers%11
end = 11-modulo
number=int(frequent_parking_number[4])
if end==number:
    print("Check digit confirmed")

#Calculating the charges
if hour_of_arrival + hours_parked >16:
    hours_before_four = (hours_parked + hour_of_arrival)
    price = 2 + (price * hours_before_four)
    if frequent_parking_number ==1:
        price = price*0.9
else:
    if frequent_parking_number ==0:
        price = price*0.5
print(price)

