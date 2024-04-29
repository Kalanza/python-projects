#typecasting = The process of converting one type of data to another
#(string,integer,float,boolean)
#explicit vs implicit
#1 Explicit typecasting.- manually conversion of a type of data from one form to another.
#Use type() function to determine the type of data type
name = "Bro" #string
age = 21 #integer
gpa = 1.9 #float
student = True#boolean

age = float(age)
print(age)
#The new value of age is 21.0 thus it is now a float
gpa = int(gpa)
print(gpa)
#The new value of gpa is 1 thus it is now an integer
student=str(student)
print(student)
#The new value of student is still True  is but now it is treated as a string.
#We can check the class using type operator
age=bool(age)
#It will return the value true
#When converting a number to a boolean it will always return true unless it is 

#Implicit type casting

#Implict Typecasting-it is the automatic conversion of a datatype from one type/class to another
#A variable data type can be converted from one form to another when you perform certain arithmetic fuctions
x = 10
y = 1.00
x = x/y
print (x)
#The new value of x will be 10.00 which is a float,this a chane from its initial form of an integer