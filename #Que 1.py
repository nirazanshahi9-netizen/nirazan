#Que 1. WAP to check whether the given number is in between 1 and 100 or not.
number = int(input("enter a number : "))
if number > 1 and number < 100:
    print("the number is in between 1 and 100")
else:
    print("the number is not in between 1 and 100")



#2 chceck whether the user input number is even or odd  and display it to user
number = int(input("enter a number : "))
if number % 2 == 0:
    print("the number is even")
else:
     print("the number is odd")


#3 wap that asks the user for a number in the range of 1 to 12 .the program should display the corresponding month,where 1 = January, 2 = February and so on.the program should display message if the user enters a number that is outside the range of 1 to 12.

number = int(input("enter a number : "))
if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Invalid input. Please enter a number between 1 and 12.")

#Method 2
number = int(input("enter a number : "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if number >= 1 and number <= 12:
    print(months[number - 1])
else:    print("Invalid input. Please enter a number between 1 and 12.")

#method 3
number = int(input("enter a number : "))
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
if number in months:
    print(months[number])
else:
    print("Invalid input. Please enter a number between 1 and 12.")

#4 A school has following rules for grading system
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A asked user to enter marks and print the corresponding grade.
marks = int(input("enter your marks : "))
if marks < 25:
    print("Grade: F")
elif marks >= 25 and marks < 45:
    print("Grade: E")
elif marks >= 45 and marks < 50:
    print("Grade: D")
elif marks >= 50 and marks < 60:
    print("Grade: C")
elif marks >= 60 and marks < 80:
    print("Grade: B")
elif marks >= 80:
    print("Grade: A")

#5 WAP to check whether a number is divisible by 7 or not
number = int(input("enter a number : "))
if number % 7 == 0:
    print("the number is divisible by 7")
else:   
    print("the number is not divisible by 7")

#6 WAP to accept two numbers and mathematical operators and perform operation accordingly.

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
operator = input("enter operator (+, -, *, /) : ")

if operator == "+":
    result = num1 + num2
    print("result :", result)
elif operator == "-":
    result = num1 - num2
    print("result :", result)
elif operator == "*":
    result = num1 * num2
    print("result :", result)
elif operator == "/":
    result = num1 / num2
    print("result :", result)
else:
    print("Invalid operator") 


#7 wite a python program to check car loan eligibility,salary >=50000 and credit score >=700 : ""eligible for car loan otherwise not eligible for car loan
salary = int(input("enter your salary : "))
credit_score = int(input("enter your credit score : "))
if salary >= 50000 and credit_score >= 700:
    print("eligible for car loan")
else:
    print("not eligible for car loan")


#8Write a Python program that takes an integer input n n. from given number check if it is divisible by both 3 and 5, then print "fizzbuzz if true.if the number is divisible by 5,print "buzz".if the number is divisible by 3, print "fizz".if the number is not divisible by either 3 or 5, print the number itself.
n = int(input("enter a number : "))
if n % 3 == 0 and n % 5 == 0:
    print("fizzbuzz")
elif n % 5 == 0:
    print("buzz")
elif n % 3 == 0:
    print("fizz")
else:    
    print(n)


#9 write a python program that takes a character input and checks whether it is a vowel or consonant.
char = input("enter a character : ")
if char in "aeiouAEIOU":
    print("the character is a vowel")
else:    
    print("the character is a consonant")


#10 write a python program to input marks and determine the grade based on the following conditions:
# a. 90-100 : A
#b. 80-89 : B
#c. 70-79 : C
#d. below 70 : F
marks = int(input("enter your marks : "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Grade: F")   


#11 write a python program to categorize a person's age :
Age < 13 : "child"
13 <= Age < 20 : "teenager"
Age >19 : "adult"
age = int(input("enter your age : "))
if age < 13:
    print("child")
elif 13 <= age < 20:
    print("teenager")
else:    
    print("adult")


#12 write a python program to check if a given character is an uppercase letter, lowercase letter,or a digit.
char = input("enter a character : ")
if char.isupper():
    print("the character is an uppercase letter")
elif char.islower():
    print("the character is a lowercase letter")
elif char.isdigit():
    print("the character is a digit")
else:    
    print("the character is not an uppercase letter, lowercase letter, or a digit")




#13 write a python program that takes a color as input (Red,yellow, green) and outputs the corresponding action(stop, ready, go).
color = input("enter a color (Red, Yellow, Green) : ")
if color.lower() == "red":
    print("stop")
elif color.lower() == "yellow":
    print("ready")
elif color.lower() == "green":
    print("go")
else:    
    print("Invalid color. Please enter Red, Yellow, or Green.")



#14 write a python program to check eligibility for a job based on age and experience:
# age > 18 and experience >= 2 : "eligible for job"
age = int(input("enter your age : "))
experience = int(input("enter your experience (in years) : "))
if age > 18 and experience >= 2:
    print("eligible for job")
else:
    print("not eligible for job")



#15 write a python program to give advice based based on the temperature:
# teperature > 30 : "It's a hot day, stay hydrated!"
# temperature between 15-30 : "enjoy the weather!"
# temperature < 15 : "It's a cold day, wear warm clothes!"
temperature = float(input("enter the temperature : "))
if temperature > 30:
    print("It's a hot day, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:    
    print("It's a cold day, wear warm clothes!")



#16 wite a python program that takes a menu option ("pizza","burger","pasta") and prints it's price:
# pizza : 10$
# burger : 7$
# pasta : 8$
menu_option = input("enter a menu option (pizza, burger, pasta) : ")
if menu_option.lower() == "pizza":
    print("you selected pizza")
    print("Price: $10")
elif menu_option.lower() == "burger":
    print("you selected burger")
elif menu_option.lower() == "pasta":
    print("you selected pasta")
else:    
    print("Invalid menu option. Please enter pizza, burger, or pasta.")



#17 wite a python program to select players based on their heights:
#height >=6 feet : "selected"
#height < 6 feet : "not selected"
height = float(input("enter your height in feet : "))
if height >= 6:
    print("selected")
else:    
    print("not selected")


#18 write a python program to check if a person is eligible to watch a movie based on their age:
# age >= 18 : "eligible to watch the movie"
# age < 18 : "not eligible to watch the movie"
age = int(input("enter your age : "))
if age >= 18:
    print("eligible to watch the movie")
else:    
    print("not eligible to watch the movie")



#19 Write a Python program to check login credentials:

#Username: "admin", Password: "password123"

#If correct, print "Access Granted"; otherwise, print "Access Denied.
username = input("enter username : ")
password = input("enter password : ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:    
    print("Access Denied")


#20 Write a Python program that takes a month number (1–12) and outputs the corresponding season:

#12, 1, 2: "Winter"

#3, 4, 5: "Spring"

#6, 7, 8: "Summer"

#9, 10, 11: "Autumn"
month = int(input("enter a month number (1-12) : "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:    
    print("Invalid month number. Please enter a number between 1 and 12.")
    