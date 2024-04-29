#python project that calculates the area of a square,rectangle,triangle and a circle.
import math
def area():
 side = 0
 length = 0
 width = 0
 height = 0
 base = 0
 radius = 0
print("Select shape you want to calculate its area")
print("1) Square")
print("2)Rectangle")
print("3)Triangle")
print("4)circle")
print("5)Quit")
x= int(input("Select enter the choice:"))
if x == 1:
    length = int(input("Enter the length:"))
    Area = length * length
elif x == 2:
    length = int(input("Enter the height:"))
    width = int(input("Enter the width:"))  
    Area = length * width
elif x == 3:
    height = float(input("Enter the height:"))
    base = float(input("Enter the base:"))  
    Area = 0.5 * base * height
elif x == 4:
    radius = float(input("Enter the radius:"))
    Area = 3.142 * radius * radius
else:
    print("Enter the valid choice:")

print("The area is",(Area))

area()
    