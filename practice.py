 
#Data types in python 
fname = "Devinton"
age = 40
isTall = False
height = 5.9

print(fname + "is a Faculty in Aptech with an average height of "+ str(height) + " and he is about " + str(age) + " years of age.")

#Operators
#Arithemetic Operator
x, y = 5, 7
print("Add", x + y) #add
print("Subtract", x - y) #sub
print("Multiply", x * y) #multiplies
print("Divide", x / y) #divides
print("Modulo", x % y) #gets the remainder as the value
print("Power", x ** y)#is used as power
print("Divide", x // y)#does the division and gets the whole number only
#Assignment Operator
x += 2
y -= 4
z = x * y
print("result: ", z)
#Comparison Operator
print("is ", x, "greater than ", y, " =", x>y)
print("is ", x, "greater and equal =", y, x>=y)
print("is ", x, "lesser than =", y, x<y)
print("is ", x, "lesser and equal =",y, x<=y)
print("is ", x, "equal =",y, x==y)
print("", x!=y)

#Logical Operator
#and

if(age>20 and age<=60):
    print("You are eligible to vote..")
else:
    print("Sorry! You cannot vote")

print("Lenght of my name", len(fname))
if(len(fname) > 3 and len(fname) <=10 ):
    print("Usual name")
else:
    print("Unusual name")
#or
newName = str(input("Enter your name: "))
if(newName == "Devinton" or newName=="Santo" or newName=="Oluchi"):
    print("Access granted")
else:
    print("Access denied")
#not
if(not isTall):
    print("Invert of false")
#Unary Operator
newAge = int(input("Enter your age: "))
print(newAge)
#Bitwise Operator
#& | ^
a, b = 5, 8

print("Bitwise and", a&b)
print("Bitwise or", a|b)
print("Bitwise xor", a^b)
print("Bitwise not", ~b)
print("Bitwise not", ~a)





