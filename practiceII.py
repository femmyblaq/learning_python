# write a python program that calculates the area and
#perimeter of all shapes and if the shape has a circumference 
#or volume and surface area, calculate for it as well.
#the shapes are (Squre, Rectangle, Triangle, Circle, Parallelogram, 
#Trapezium, Rhombus, Kite, Cube, Cuboid, Shere, Cylinder, Cone, Hemisphere,
#Pyramid),

print("\t\tBASIC SHAPES AND THEIR FORMULAS..")
print("Select which shape you want to find the Area, Perimeter, Circumference,Volume, Surface area.\n")
print("1.) Square")
print("2.) Rectangle")
print("3.) Triangle")
print("4.) Circle")
print("5.) Parallelogram")
print("6.) Trapezium")
print("7.) Rhombus")
print("8.) Kite")
print("9.) Cube")
print("10.) Cuboid")
print("11.) Sphere")
print("12.) Cylinder")
print("13.) Cone")
print("14.) Hemisphere")
print("15.) Pyramid\n\n") 

# area, perimeter, circumference 
# volumesurface, area

area = 0.0
perimeter = 0.0
circumference = 0.0
PI = 3.141529
choice = int(input("Enter choice of shape: "))
match (choice):
    case 1:
        print("THE AREA AND PERIMETER OF A SQUARE")
        a = float(input("Enter value for a: "))
        area = a ** 2
        perimeter = 4 * a
        print(f"The area of the value {a} is: {area}.\nThe perimeter is: {perimeter}")
    case 2:
        print("THE AREA AND PERIMETER OF A RECTANGLE")
        l = float(input("Enter length:"))
        w = float(input("Enter width:"))
        area = l * w
        perimeter = 2(l * w)
        print(f"The area of the value {l} and {w} is: {area}.\nThe perimeter is: {perimeter}")
    case 3:
        print("THE AREA AND PERIMETER OF A TRIANGLE")
        base = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = (1/2) * base * h
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        c = float(input("Enter value for c: "))
        perimeter =  (a+b+c) / 2
        print(f"The area of the value {base} and {h} is: {area}.\nThe perimeter is: {perimeter}")
    case 4: 
        print("THE AREA AND CIRCUMFERENCE OF A CIRCLE")
        r = float(input("Enter value for radius: "))
        area = PI * pow(r, r)
        circumference = 2*PI*r
        print(f"The area of the value {r} is: {area}.\nThe circumference is: {circumference}")
    case 5:
        print("THE AREA AND PERIMETER OF A PARALLELOGRAM")
        
