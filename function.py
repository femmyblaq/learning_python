# def calculate(a, b, op): 
#     match op:
#         case '+':
#             return a + b
#         case '-':
#             return a - b
#         case '*':
#             return a * b
#         case '/':
#             return a / b
#         case '**':
#             return a ** b
#         case '//':
#             return a // b
#         case '%':
#             return a % b
#         case _: print("Sorry, enter a valid operator (+, -, *, /, %, **, //)...")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))


# op = str(input("Enter operator: "))
# while(op != "+" and op != "-" and op != "*" and op != "/" and op != "**" and op != "//"):
#     print("Sorry, enter a valid operator (+, -, *, /, %, **, //)...")
#     op = str(input("Enter operator: "))
# result = calculate(a, b, op)
# print("Result: ", result)


# Create a simple banking system that accepts user name (first and last)
# a function that allows the user to deposit, check balance, withdraw, set pin

# Lambda Function
# square = lambda x: x * x
# sum = lambda a, b: a + b

# print(square(5))
# print(sum(5, 4))
# numbers = [3, 4, 5, 6, 3]
# sqr = list(map(lambda x: x ** 2, numbers))


# simpleCalc = {
#     "add": lambda x, y: x+y, 
#     "sub": lambda x, y: x-y, 
#     "mul": lambda x, y: x*y, 
#     "div": lambda x, y: x/y 
# }

# print("multiplication: ", simpleCalc["mul"](5, 6))
# print(simpleCalc["add"](9, 9))
# print(simpleCalc["div"](8, 2))
# print(sqr)

# #Class 
# class MyClass:
#     def __init__ (s, fname, lname):
#         s.fname = fname
#         s.lname = lname

#     def __str__ (s):
#         return f"{s.lname} - {s.fname}"
    
# p1 = MyClass("Bill", "Gate")
# p2 = MyClass("Alice", "William")
# p3 = MyClass("Jason", "Doe")

# print(p1)
# print(p2)
# print(p3)

# class Student:
#     def __init__(s, stName, stId):
#         s.stName= stName
#         s.stId= stId
#         s.courses = []
    
#     def enroll(s, courseName):
#         if courseName not in s.courses:
#             s.courses.append(courseName)
#             print(f"{s.stName} enrolled for {courseName}")
#         else:
#             print(f"{s.stName} has already enrolled for this course.")
#     def remove(s, courseName):
#         if courseName in s.courses:
#             s.courses.remove(courseName)
#             print(f"{s.stName} removed this {courseName}")
#         else:
#             print(f"{s.stName} course you are trying to remove does not exist.")

#     def listCourse(s):
#         return s.courses
            
# student_name = str(input("Enter your full name: "))
# student_id = str(input("Enter your student Id: "))
# student1 = Student(student_name, student_id)
# print("\n")
# courseNumber = int(input("How many course would you like to enroll for: "))
# for i in range(0, courseNumber):
#     course = str(input("Enter course: "))
#     student1.enroll(course) 




# print("1. Would you like to change a course? (yes / no) or (y/n)")
# print("2. Would you like to remove a course? (yes / no) or (y/n)")
# userChoice = str(input())
# match userChoice.lower():
#     case "yes" | "y":
#         rmCourse = str(input("Which course would you like to remove? "))
#         student1.remove(rmCourse)
#     case "no" | "n":
#         print("Thank you for your time.")


# print(student1.listCourse())


class Vehicle: 
    def __init__(s, name, color):
        s.name = name
        s.price = 500
        s.is_available = True
        s.color = color

    def rent(s):
        if s.is_available:
            match s.name:
                case "Lambogini":
                    s.price= 2000
                    print(f"This would cost you ${s.price}")
                case "Ferrari":
                    s.price= 2500
                    print(f"This would cost you ${s.price}")
                case "Cyber Truck":
                    s.price= 1800
                    print(f"This would cost you ${s.price}")
            choice = str(input("Would you like to proceed?"))
            match choice:
                case "yes" | "y":
                    print(f"{s.color} {s.name}  has been rented.")
                case "no" | "n":
                    print("Select a car price within your budget.")
                    
            
            s.is_available = False 
        else:
            print(f"{s.name} is not available")
    def return_vehicle(s):
        s.is_available = True
        print(f"{s.name} has been returned.")


print("Would you like to rent a vehicle (yes/no) (y/n):")
choice = str(input())

match choice.lower():
    case "yes" | "y":
        carName = str(input("What type of car would you like to rent? "))
        carColor = str(input("What color of car would you prefer? "))
        
        car1=Vehicle(carName, carColor)
    case "no" | "n":
        print("Thank you for your time.")

print(car1.rent())



#Create a Library of books where user can add books, borrow books, list all available books return book,