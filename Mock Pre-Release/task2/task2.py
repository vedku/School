#variables
days = [1,2,3,4,5,6,7]
time_arrived = []
hours_parked = []
frequent_parking_number = []
timings = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
price = 1
pph1 = 2
pph2 = 2
pph3 = 2
pph4 = 2
pph5 = 2
pph6 = 4
pph7 = 8
amount_paid = 0

#questions
print("The day of the week is represented by a number. For example, monday is 1. Accordingly answer the question using numbers ranging from 1 to 7")
day = int(input("What day is it?:"))
print("ONLY INPUT THE HOUR OF ARRIVAL, EXCLUDE MINUTES. FOR EXAMPLE 15:45 becomes 15. USE 24 hour time")
time_arrived = int(input("What time have you arrived at?:"))

#validation for hours parked in a day
hours_parked = int(input("How many hours did you park for?:"))
while day ==1 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Monday. \nHow many hours did you park for?:"))
while day ==2 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Tuesday. \nHow many hours did you park for?:"))
while day ==3 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Wednesday. \nHow many hours did you park for?:"))
while day ==4 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Thursday. \nHow many hours did you park for?:"))
while day ==5 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >2:
    hours_parked = int(input("You can't park for more than two hours on a Friday. \nHow many hours did you park for?:"))
while day ==6 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >4:
    hours_parked = int(input("You can't park for more than two hours on a Saturday. \nHow many hours did you park for?:"))
while day ==7 and  time_arrived in  [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and hours_parked >8:
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
    print("Check digit confirmed, you are eligible for a discount!")

#Calculating the charges
if day == 1:
    price = (hours_parked*pph1)
elif day == 2:
    price = (hours_parked*pph2)
elif day == 3:
    price = (hours_parked*pph3)
elif day == 4:
    price = (hours_parked*pph4)
elif day == 4:
    price = (hours_parked*pph4)
elif day == 5:
    price = (hours_parked*pph5)
elif day == 6:
    price = (hours_parked*pph6)
elif day == 7:
    price = (hours_parked*pph7)
if time_arrived >16 and time_arrived <23 and end==number:
    price = (price*0.5)
else:
    price = (price*0.9)
print("Your price after a discount is: $",price)

#task2|daily total of payments made for parking
amount_paid = int(input("please pay here:"))
if amount_paid <= price:
    amount_paid = int(input("insufficient funds, pay again:"))


