
#Method 1: Using if-else statements to validate user input for a registration form
first_name =input("enter your first name: ")
last_name =input("enter your last name: ")
email =input("enter your email: ")
re_email =input("re-enter your email: ")
password =input("enter your password: ")
if not(first_name and last_name and email and re_email and password):
    print("All fields are required.")
elif not((first_name.isalpha() and last_name.isalpha()) and (email == re_email) and (password is len(password) >= 6)):
    print("Invalid input. Please check your details and try again.")
else:
    print("Registration successful!")
    

#Method 2:
first_name =input("enter your first name: ")
last_name =input("enter your last name: ")
email =input("enter your email: ")
re_email =input("re-enter your email: ")
password =input("enter your password: ")

if not(first_name and last_name and email and re_email and password):
    print("All fields are required.")
    is_valid = False
elif not((first_name.isalpha() and last_name.isalpha())):
    print("First name and last name should contain only letters.")
    is_valid = False
elif email != re_email:
    print("Email addresses do not match.")
    is_valid = False
elif len(password) < 6:
    print("Password should be at least 6 characters long.")
    is_valid = False
else:
    print("Registration successful!")
    is_valid = True


