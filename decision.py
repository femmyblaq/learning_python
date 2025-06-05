num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("This is an even number.")
else: 
    print("This number is not an even number")



if(num % 2 == 0 and num % 3 == 0):
    print("Hello World")
elif(num % 2 == 0):
    print("Hello")
elif(num % 3 == 0):
    print("World")
else: print("No place for this")

if(num == 1):
    print("It's Monday")
elif(num == 2):
    print("It's Tuesday")
elif(num == 3):
    print("It's Wednesday")
elif(num == 4):
    print("It's Thursday")
elif(num == 5):
    print("It's Friday")


day = input("Enter a letter in day: ")
match str(day):
    case 'S':
        print("Sunday")
    case 'm' | 'M':
        print("Monday")
    case 'T':
        print("Tuesday")
    case 'w' | 'W':
        print("Wednesday")
    case 't':
        print("Thursday")
    case 's':
        print("Saturday")
    case _: print("Sorry your character has no match.")
    
i=1
while(i<5):
    print(i)
    i+=1


