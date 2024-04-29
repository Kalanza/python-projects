import My_module as mm 
import sys
courses = ['History','Math','Physics','CompSci']

index = mm.find_index(courses,'Math')
print(index)
#print(test)
#We can import a specific function directly from the python file
from My_module import find_index , test

courses = ['History','Math','Physics','CompSci']

index = find_index(courses,'Math')
print(index)
print(test)
#The results will be similar but the second one saves on space
print(sys.path)
#Shows us the file/python path used to trace and link this file with My_module.py

#An example of a standard module library
import random 
courses = ['History','Math','Physics','CompSci']
random_course = random.choice(courses)
print(random_course)

import math
#Enables us to carry out any arithmetic computation

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
#This two enable us to workk with dates,time and yeard
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

import os
#It enables us to ccess the os and carry out various fuctions such as creating and deleting files
print(os.getcwd())
print(os.__file__)#prints out the location of the file and prints out the entire standard library
#dunder file attribute


