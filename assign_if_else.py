#1 A theme park has these rules:You can ride the roller coster if you are at least 12 years old and at least 140cm tall Write the if-else code for this.
age = int(input("enter your age : "))
height = int(input("enter your height in cm : "))
if age >= 12 and height >= 140:
    print("You can ride the roller coaster.")
else:
    print("You cannot ride the roller coaster.")


#2 Design a traffic light system .given a variable light that can be red,yellow or green,print the correct instruction.also handle an invalid color with an error message.
light = input("enter the traffic light color (red, yellow, green) : ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")

#method 2 using match case statement
light = input("enter the traffic light color (red, yellow, green) : ")
match light.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color. Please enter red, yellow, or green.")


#3 write a match statement that takes a number 1-4 and prints the corresponding season: 1=spring, 2=summer, 3=autumn, 4=winter. default "unknown "
number = int(input("enter a number : "))
match number:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autumn")
    case 4:
        print("winter")
    case _:
        print("unknown")

#4 write a login system using nested if .check -if username equals "admin".inside that,if password equals "pass123"
username = input("enter username : ")
password = input("enter password : ")
if username == "admin":
    if password == "pass123":
        print("Login successful.")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")

#5 Design a bank loan approval system.Approve a loan only if all three conditions are met: Age is between 21 and 60 inclsive,Monthly income is at least 30000,credit score is at least 700.
age = int(input("enter your age : "))
income = float(input("enter your monthly income : "))
credit_score = int(input("enter your credit score : "))
if 21 <= age <= 60 and income >= 30000 and credit_score >= 700:
    print("Loan approved.")
else:
    print("Loan not approved.")


#6 You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person and whether they have a membership card. If the person is under 12, the ticket is free. If the person is between 12 and 60: If they have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs. 200. If the person is above 60, they get a senior citizen discount, and the ticket costs Rs. 100. Write a Python program using nested if-else to calculate and print the ticket price based on the user's age and membership status.
age = int(input("enter your age : "))
membership = input("do you have a membership card? (yes/no) : ")
if age < 12:
    print("Ticket price: Free")
elif 12 <= age <= 60:
    if membership == "yes":
        print("Ticket price: Rs. 150")
    else:
        print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 100")


#7 A company gives a 5% bonus to employees if their years of service are more than 5 years. Ask the user for their salary and years of service, then print the net bonus amount
salary = float(input("enter your salary : "))
years_of_service = int(input("enter your years of service : "))
if years_of_service > 5:
    bonus = salary * 0.05
    print(f"Net bonus amount: Rs. {bonus:.2f}")
else:
    print("No bonus awarded.")


#8 write a python program which accepts the radius of circle from user and calculate the area.
import math
radius = float(input("enter the radius of the circle : "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area:.2f}")


#10. Accept input from user
#If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of number
#If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
#If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
#If given number is not multiple of 3 or 5 prints value as usual."
number = int(input("enter a number : "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

