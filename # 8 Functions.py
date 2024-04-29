#def is used when declaring a function and passing arguments.
#parameter - input you define for your function
#argument - actual value of a parameter.
#Two types of functions
#1 -Perform a task 
#2 -Return a value
def greet(First_name,Last_name):
    print(f"Hello {First_name} '+ '{Last_name}")
greet("Victor","Kalanza")
#It displays the words Hello Victor Kalanza

def greet(name):
  print(f"Hi {name}")
greet("mosh")

#Key word arguments
#They are used for purposes of clarity
#In the following code number = 3 is an example of a keyword argument.
def increment (number,by):
   return number + by
result = increment(number = 3,by = 7)
print (result)

#Optional parameters 
#They should come after the required parameter
def increment (number,by=1):
    return number + by
result = increment(number = 3)
print (result)

#Functions enable us to reuse code without repeating ourselves
def hello_func():
    print("Hello world")
    pass
#This shows that the function will be declared later
hello_func()
def hello_func(greeting,name ='you'):#greeting,name ='you' are parameters.
    return'{},{}'.format(greeting, name)
print(hello_func('Hi',name ='Corey'))
#It returns Hi,corey
#This shows how to pass arguments in a function

 # Kwargs / **(double aisterics) can be used to pass multiple keyword arguments
 # Args / *(single aistercs) can be used to pass positional arguments
def student_info(*args,**kwargs):
    print(args)#it displays('Math','Art')
    print(kwargs)#it displays {'name':'John','age":22}
    #it allows us to  accept an arbitrary number of positional and keyword arguments
    student_info('Math','Art',name='John',age=22)
  
  
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
    courses=['Math','Art']
    info = {'name': 'John', 'age':22}
    student_info(*courses,**info)#This argument/parameter unpacks the values
    #A Sample code for calculating a leap year
    """Number of days per month.First value placeholder  for indexing purposes."""
    month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    def is_leap(year):
        """Return True for leap years, False for non-leap years."""
        #This are doc strings and are used to document what a function should do
        return year %4 == 0 and (year % 100 != 0 or year % 400 ==0)
    def days_in_month(year,month):
        """Return no of days in that month in that year"""
        if not 1 <= month <+ 12:
            return 'Invalid Month'
        if month == 2 and is_leap(year):
            return 29
        return month_days[month]
    print(is_leap(2017))
    print(is_leap(2020))
    print(days_in_month(2017,2))
    print(days_in_month(2020,2))
    