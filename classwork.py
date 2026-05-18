#2
# shopping_list ={"milk","bread","eggs"}
# bought ={"bread","eggs"}
# unbought =shopping_list.difference(bought)
# if unbought:
#     print("unbought items:",unbought)
# else:
#     print("shopping complete")


# #1
# records ={'samrat':'samrat@gmail.com'}
# user_name = input("enter a name:")
# if user_name in records:
#     print(f'email of{user_name}:{records[user_name]}')
# else:
#     print("contact not found")


# #3
# classlist = ['ram','sita','laxman']
# new_student = input("students to be added:")
# if new_student in classlist:
#     print("student is already present.")
# else:
#     classlist = classlist.append(new_student)
#     print("student added to the list.")

# #4
# votes =["blue","red","blue","green","blue"]
# a = votes.count("blue")
# if a>=3:
#     print("blue wins")
# else:
#     print("blue doesn't win")

# #5
# grades ={'ram':92,'sita':88}
# st_in = input("enter student name:")
# check = st_in in grades
# if check:
#     print(grades.get(st_in))
# else:
#     print('grade not available')

# #6
# applicant = {"name":"priya","skills":["java","SQL"],"experience_years":1}
# required_skills = {"python","java"}
# if not (required_skills.isdisjoint(applicant["skills"])) and applicant:

#  print('priya doesnot qualifie')
# else:
#     print("priya  qualify")

# #7
# banned_items = {"scissors","knife","lighter"}
# baggage_weight = int(input("enter baggage weight:"))
# items_in_baggage = input("enters the item in baggage:").lower()
# if baggage_weight<=7 and items_in_baggage not in banned_items:
#     print("the bage is allowed")
# else:
#     print("the baggage is not allowed")

# #8
sample_dict = {
    'emp1':{'name':'john','salary':7500},
    'emp2':{'name':'Emma','Salary':8000},
    'emp3':{'name':'Shyam','salary':500}
}
for emp in sample_dict.values():
    if emp['name']== 'shyam':
        emp['salary'] = 7500

#9
nirajan_items ={"noodle","biscuit","pasta","mango"}
shyam_items ={"apple","orange","watermelon","banana"}
if nirajan_items.isdisjoint(shyam_items):
    print("they picked completely different items")
else:
    print("they have some common items")

#10
list = [10,20,30]
tuple =(10,20,30)
set = {10,15,20}
dict = {'a','10','b',20}
val = 20
if val in list and val in tuple:
    if 'b' in dict and val not in set:
        print("verified token routed")
        print("path A")
    else:
        print("Access denied / Route Diverted")
        print("path B")
else:
    print("system reject token")
    print("path c")

#16
menu = {
    'Pizza': 450,
    'Burger': 300,
    'Salad': 200
}
order = 'Pizza'

if order in menu:
    print(f"The price of {order} is Rs{menu[order]}")
else:
    print("Item not found")

#17
student_data = {"name": "Sam", "score": 85}
if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)


#18
database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")

#19
emails = ['samrat7@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'samrat7@gmail.com'}
current_email = 'samrat7@test.com'

if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")

#20
inventory        = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target           = 'B2'


if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")

else:
    print("invalid zone")


#21
valid_courses= {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]

name   = input("Enter student name: ")
course = input("Enter course (python/robotics/java): ").lower()
grade  = int(input("Enter grade (9-12): "))

student_record = {
    "name"  : name,
    "course": course,
    "grade" : grade
}
if course not in valid_courses:
    print(f"{name} selected an invalid course.")

elif grade < 9:
    print(f"Grade too low.")

elif grade > 12:
    print(f"Grade too high.")

else:
    if course == 'robotics' and grade == 9:
        print(f"{name} is not eligible for {course}, grade too low.")
    else:
        print(f"{name} is approved for {course}.")

