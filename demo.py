# first_name = input("enter your first name : ")
# last_name = input("enter your last name : ")
# email=input("enter your email : ")
# re_email=input("re-enter your email : ")
# password=input("enter your password : ")
# if not (first_name and last_name and email and re_email and password):
#     print("All fields are required.")
# elif not(first_name.isalpha() and last_name.isalpha()):
#     print('must enter or type letters only')
# elif not ('@' in email and '.' in email):
#     print("invalid email format")
# elif email != re_email:
#     print("emails do not match")
# elif len(password) < 8:
#     print("password must be at least 8 characters long")
# else:
#     print("Registration successful.")




'''# hand sign game'''
# player1 = input("player 1, enter your hand sign (rock, paper, scissors) : ")
# player2 = input("player 2, enter your hand sign (rock, paper, scissors) : ")
# if player1 == player
#     print("It's a tie!")
# elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
#     print("Player 1 wins!")
# elif (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
#     print("Player 2 wins!")



balance =20000
correct_pin = 3796
print("Welcome to the ATM!")
user_pin = int(input("Please enter your PIN: "))
if user_pin == correct_pin:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. exit")
    choice = int(input("Please select an option(1-3): "))
    if choice == 1:
        print(f"Your balance is: Rs. {balance}")
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            if amount <=0:
                print("Invalid amount. Please enter a positive number.")
            print(f"Withdrawal successful. Your new balance is: Rs. {balance}")
        else:
            print("Insufficient funds.")
    elif choice == 3:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid option. Please select 1, 2, or 3.")
else:
    print("Incorrect PIN. Access denied.")

