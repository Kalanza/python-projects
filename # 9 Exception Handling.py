#exceptions and error handling in python
#There are different typs of errors such as(ie. print 9/0 ) zero division error,value error etc.
#Not every exception is of the same kind.
#We can use try and except function to handle exceptions
#We use the input function when we want store a number in  variable
# finally : the code after this word is always executed whether tere is an exception or not
try:
    x = int(input("First number:"))
    y = int(input("Second number"))
    print(x/y)
except:
    print("THERE WAS AN ERROR!")
if ValueError:
   print("Enter a valid number")
if ZeroDivisionError:
    print("No number can be divided by zero")
    #Incase of an error it will print there was an error but the program won't be terminated 
    #so the next block of code will be executed
    #For example consider the following code
    def mysum(x,y):
        return pow(x,y)
    result = pow(10,2)
print (result)
#if you input the first number as a string for example First number:victor a value error will occur but instead of the program crushing
#it will display the message - THERE WAS AN ERROR! 
#The interpreter will move to the next block of code and then execute it if there is no error
# it will display the value 100
#You can specify what type of message you want to be displayed depending on the type of error.
#for example in the code above if the error is a ValueError it will display the following message
#"Enter a valid number"
#for example in the code above if the error is a zERODivisionError it will display the following message
#No number can be divided by zero"

    