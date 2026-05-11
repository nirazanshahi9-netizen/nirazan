#5
total_purchase_amount = int(input("Enter the total purchase amount: "))
if total_purchase_amount > 5000:
    membership_status = input("Are you a member? (yes/no): ").lower()
    if membership_status.lower() == "yes":
        discount = total_purchase_amount * 0.30
        final_amount = total_purchase_amount - discount
        print (f"total saved :{discount}")
        print (f"final :{final_amount}")
    else:
        print(f"total: {total_purchase_amount}")
        print("discount: 0")
else:
        print(f"total: {total_purchase_amount}")
        print("discount: 0")


#6 
print("welcome to the magic forest")
stage_1 = input("go north or south : ").lower()
if stage_1 == "north":
     stage_2 = input("cross the river or follow the path :").lower()
     if stage_2 =="follow the path":
          stage_3 =input("choose: fairy, org or elf :").lower()
          if stage_3 == "elf":
                print("you win")
                print("game over")
          else:
                print("you lose")
                print("game over")
else:
                print("you lose")
                print("game over")



#question 1
i =int(input("enter a number : "))
j =int(input("enter a number : "))
k =int(input("enter a number : "))
if i<j:
    if j<k:
        i = j
    else:
          j = k
else:
    if j>k:
        j = i 
    else:
        i = k
        print(i,j,k)


# a)i =3, j =5, k =7
# Is 3<5? Yes, enter if 
# Is 5<7? Yes, enter i=j
# i becomes 5
# output: 5 5 7

# b) i=2, j=-5,k=9
# Is -2<-5? No, enter else
# Is -5>9? No, enter else
# i becomes 9
# output: 9 -5 9

# C) I=8,J=15,K=12
# Is 8<15? Yes, enter if
# Is 15<12? No, enter else
# J=K
# j becomes 12
# output: 8 12 12

# D) I=13,J=15,K=13
# Is 13<15? Yes, enter if
# Is 15<13? No, enter else
# J=K
# j becomes 13
# output: 13 13 13

# E) I=3,J=5,K=7
# Is 3<5? Yes, enter if
# Is 5<7? Yes, enter i=j
# i becomes 5
# output: 5 5 7

# F) I=25,J=15,K=17
# Is 25<15? No, enter else
# Is 15>17? No, enter else
# i=K
# i becomes 17
# output: 17 15 17

# question 10
body_weight= float(input("Enter your bodyweight:"))
height=float(input("Enter your Height:"))
BMI=float(body_weight/(height**2))
if BMI<18.5:
     print("You are underweight")
elif BMI<25:
     print ("You have normal weight")
elif BMI<30:
     print("You are overweight")
else:
     print("You are Obese")
print(f"Weight: {body_weight}")
print(f"Height: {height}")
print(f"BMI: {BMI}")

# question 15
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    # Multiple of both 3 and 5
    print("Fizz Buzz")
elif number % 3 == 0:
    # Multiple of 3 only
    print("Fizz")
elif number % 5 == 0:
    # Multiple of 5 only
    print("Buzz")
else:
    # Not a multiple of 3 or 5
    print(number)


#question 16
usage = float(input("Enter electricity usage (in units): "))

if usage < 100:
    cost = usage * 5
    
elif usage <= 300:
    cost = (100 * 5) + ((usage - 100) * 8)
    
else:
    cost = (100 * 5) + (200 * 8) + ((usage - 300) * 10)
print(f"Electricity Usage: {usage} units")
print(f"Total Cost: Rs {cost:.2f}")
print("="*40)

if usage < 100:
    print(f"  {usage} units @ Rs 5 = Rs {usage * 5:.2f}")
elif usage <= 300:
    print(f"  First 100 units @ Rs 5 = Rs {100 * 5:.2f}")
    print(f"  Next {usage - 100} units @ Rs 8 = Rs {(usage - 100) * 8:.2f}")
else:
    print(f"  First 100 units @ Rs 5 = Rs {100 * 5:.2f}")
    print(f"  Next 200 units @ Rs 8 = Rs {200 * 8:.2f}")
    print(f"  Remaining {usage - 300} units @ Rs 10 = Rs {(usage - 300) * 10:.2f}")
print(f"\n  Total: Rs {cost:.2f}")


# question 20
print("WEIGHT CONVERSION - CALCULATE YOUR WEIGHT ON OTHER PLANETS")

earth_weight = float(input("Enter your Earth weight (in kg): "))
planet_number = int(input("\nSelect a planet:\n1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune\nEnter planet number (1-8): "))

if planet_number == 1:
    destination_weight = earth_weight * 0.38
    planet_name = "Mercury"
elif planet_number == 2:
    destination_weight = earth_weight * 0.91
    planet_name = "Venus"
elif planet_number == 3:
    destination_weight = earth_weight * 1.0
    planet_name = "Earth"
elif planet_number == 4:
    destination_weight = earth_weight * 0.38
    planet_name = "Mars"
elif planet_number == 5:
    destination_weight = earth_weight * 2.34
    planet_name = "Jupiter"
elif planet_number == 6:
    destination_weight = earth_weight * 1.06
    planet_name = "Saturn"
elif planet_number == 7:
    destination_weight = earth_weight * 0.92
    planet_name = "Uranus"
elif planet_number == 8:
    destination_weight = earth_weight * 1.19
    planet_name = "Neptune"
else:
    print("Invalid planet number! Please enter a number between 1 and 8.")
    destination_weight = None
    planet_name = None

if destination_weight is not None:
    print("\n" + "="*60)
    print(f"Your Earth weight: {earth_weight} kg")
    print(f"Your weight on {planet_name}: {destination_weight:.2f} kg")
    print("="*60)


