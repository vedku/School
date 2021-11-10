""" validation or verification
This program is a fun way to play with validation and verification.


Coding you don't need to know for iGCSE
Most of the code I've tried to keep to iGCSE level. Here are the exceptions:

* Functions are AS level.
* Students don't NEED to program try and except. However it makes programs much more resilient.
* The ord command isn't needed for iGCSE but makes it easy to check ASCII back to numbers
* Random and datetime are used for the game and aren't needed in iGCSE programming

validation checks
* range checks range_check()
* character checks character_check()
* check digits check_digit()
* format checks format_check()
* length checks length_check()
* presence checks presence_check()
* type checks type_check()

verification checks
* double entry double_entry()
* screen / visual check visual_check()
* parity check parity_check()
* checksum checksum()

"""

import random
import datetime

validation = ["range checks","character checks","check digits","format checks","length checks","presence checks","type checks",]
verification = ["double entry","screen or visual check","parity check","checksum"]


# validation

def range_check():
    """Checks that numbers are within a specific range """
    while True:
        x=int(input("please enter a number from 1 to 5: "))
        if x<1 or x>5:
            print("failed")
        else:
            print("passed")
            break

def character_check():
    validation = True
    x = input("Please enter a phone number?")
    for i in x:
        print(i)
        if i in ["0","1","2","3","4","5","6","7","8","9"," ","+"]:
            print("OK")
        else:
            print("X")
            validation = False
    if validation == True:
        print("passed")
    else:
        print("failed")


def check_digit():
    multiplier = 1 #alternates between 1 and 3
    total = 0
    print("An example ISBN is 978-0-545-01022-1")
    isbn = input("Input an ISBN-13")

    #This removes dashes
    isbn=isbn.replace("-","")

    #the last digit is the check digit
    try:
        check_digit=int(isbn[12])
        print("final digit",check_digit)
        for i in range(12):
            total = total + (int(isbn[i])*multiplier)
            if multiplier == 1:
                multiplier = 3
            else:
                multiplier = 1
        remainder = total % 10
        print("remainder",remainder)
        if (10-remainder) == check_digit:
            print("ISBN passed")
        else:
            print("ISBN failed")
    except:
        print("That was nothing like an ISBN")

def format_check():
    print("postcode example CB2 8EA")
    postcode = input("Please input a UK postcode")
    length = len(postcode)
    # This checks the overall length.
    if length > 8 or length < 6:
        print("Failed format check, length wrong")
    #Because the front characters can change, this works from the end to check for the space.
    elif (postcode[length-4])==" ":
        print("passed")
    else:
        print("Failed, space in wrong place")

def length_check():
    while True:
        x = input("Please enter a year")
        if len(x)==4:
            print("passed")
            break
        else:
            print("failed")

def presence_check():
    while True:
        x=input("please type something")
        if x=="":
            print("failed")
        else:
            print("check passed")
            break

def type_check():
    while True:
        MyNumber = input("Please enter a number: ")
        try:
            valid_number = int(MyNumber)
            break
        except ValueError:
            print("Seriously, don't you read the instructions. \nI asked for a number...")

#verification

def double_entry():
    while True:
        x1 = input("Please enter a word: ")
        x2 = input("Please reenter the word: ")
        if x1 == x2:
            print("passed")
            break
        else:
            print("failed")

def visual_check():
    while True:
        print("Computer Science is the best subject in the world")
        x=input("Happy with this? Y/N")
        if x.upper()== "Y":
            print("Passed")
            break
        else:
            print("Failed")

def parity_check():
    main_num = input("Please enter a binary number:")
    even_parity = input("Please enter an even parity bit")
    ones = 0
    for i in main_num:
        if i == "1":
            ones+=1
    print("Number of ones",ones)
    if ones%2 == 0:
        if even_parity=="0":
            print("Passed")
        else:
            print("Failed, not 0")
    else:
        if even_parity=="1":
            print("Passed")
        else:
            print("Failed, not 1")

def checksum():
    checksum = 0
    string = input("Enter some text:")
    for i in string:
        checksum += ord(i) #ord Gives the number for the ASCII
    print("ASCII checksum is:",checksum)

def menu_print():
    count = 1
    print("\nValidation")
    for i in validation:
        print(count,i,end=" ")
        count+=1
    print("\n\nVerification")
    for i in verification:
        print(count,i,end=" ")
        count+=1

def menu_go(chosen):
    print("\n")
    if chosen == 1: range_check()
    elif chosen == 2: character_check()
    elif chosen == 3: check_digit()
    elif chosen == 4: format_check()
    elif chosen == 5: length_check()
    elif chosen == 6: presence_check()
    elif chosen == 7: type_check()
    elif chosen == 8: double_entry()
    elif chosen == 9: visual_check()
    elif chosen == 10: parity_check()
    elif chosen == 11: checksum()
    elif chosen == 0: print("0")
    else: print("No option chosen")

def game():
    game_count=[1,2,3,4,5,6,7,8,9,10,11]
    score = 0

    for i in range(11):
        beginning = datetime.datetime.now()
        chosen=random.choice(game_count) # Using list to ensure not chosen twice.
        game_count.remove(chosen)
        print("Random validation or verification selected")
        print("Try it out!")
        menu_go(chosen)
        print("Guess the type")
        menu_print()
        x = int(input("Your guess: "))
        if x == chosen:
            end = datetime.datetime.now()
            difference=end-beginning
            bonus=difference.total_seconds()
            bonus = int((60-bonus)*100)
            print("You scored 200 points")
            print("Your timer score is",bonus)
            score += 200+bonus
            print("Your current score is:",score)
        else:
            print("It was type",chosen)

    print("\n Game finished!")
    print("Your final score is",score)

while True:
    print("\nValidation and Verification game!")
    print("Choose D for Demo, G for Game or Q quit")
    choose = input("Enter your choice: ")
    if choose.upper() == "D":
        menu_print()
        menu_go(int(input("choose an option:")))
    elif choose.upper() =="G": game()
    elif choose.upper() =="Q": quit()
