#List - Ordered, changable, duplicate.

# cars = ["Cyber Truck", "Rolls Royce", "Ferrari", "Mercedez", "Maybach"]

# cnt = 1
# while cnt <= 5:
#     enterCarName = str(input(f"Enter car name {cnt}: "))
#     if enterCarName in cars:
#         print("Sorrry car name already exist!")
#     else:
#         cars.append(enterCarName)
#         print("car added successfully!!")
#         cnt +=1



# cars.remove("Ferrari")
# cars.pop(2)
# cars.sort()
# print(cars)

# for car in cars:
#     print(car)

#Tuple
fruit1 = ("Apple", "Orange", "Melon", "Pineapple")
fruit2 = ("Cherry", "Mango", "Grapes", "Banana")
print(fruit1[1])

y = list(fruit1)
y.append("Paw Paw")
fruit1 = tuple(y)

listOfFruits = [fruit1, fruit2]

print("List of Fruits: ", listOfFruits)
print("Length: ", len(fruit1))


for f in fruit1: 
    print(f)
    


#Set
setA = {2, 4, 6, 8}
setB = {1, 3, 6, 3, 5}
setC = {"Felicia", "Jerry", "Simeon", "Ali"}

print("Union of a set: ", setB | setA)
print("Intersection of a set: ", setB & setA)
print("Difference of a set: ", setB - setA)

setC.add("Dele")
setC.discard("Dele")
# setC.update(setA)
setC.pop()
setC.union(setA)
setA.intersection(setB)
setB.difference(setA)
setB.symmetric_difference(setA)

#setA.clear()
print(setC)


#Dictionary List
questions = [{
    "type": "question1", 
    "text": "What is the capital of France?",
    "options": ["Paris", "London", "New York", "Berlin"],
    "answer": "a"

}, {
    "type": "question2", 
    "text": "What continent is America?",
    "options": ["Asia", "SA", "Africa", "N of A"],
    "answer": "b"
}, {
    "type": "question3", 
    "text": "What currency does Australians spend",
    "options": ["Naira", "Pounds", "Euro", "AD"],
    "answer": "d"
}]
score = 0
for question in questions:
    print("\n\n", question["text"])
    print("A.) ", question["options"][0], "\tB.)", question["options"][1])
    print("C.) ", question["options"][2], "\tD.)", question["options"][3])
    ansSpot = str(input("Enter Answer (a, b, c, d): "))
    if ansSpot != question["answer"]:
        print("Incorrect Answer!!")
    else: 
        print("Correct Answer!!")
        score += 3
  

print("\n\nTotal score: ", score, "\n\n")
# print(questions.get("answer"))
allP = questions.keys()
allV = questions.values()

# print(allP)
# print(allV)

# for k in questions.keys():
#     print(k)



# questions["flag"] = False
# questions["marke"] = True

# questions.pop()
# questions.update()


