#6 loops and iterations
#break statement - breaks loop 
#continue - it skips a value in a loop
nums = [1,2,3,4,5]
for number in nums:
    if number == 3:
     print("Found!")
     break
 #if you use break it will display the values 1,2 and Found! then terminate the loop
nums = [1,2,3,4,5]
for number in nums:
    if number == 3:
     print("Found!")
     continue
 #if you use continue the loop will ignore the value 3 and then continue with the iteration
 #nit will print the values 1 2 found! 4 5
     print(num)

#7 nested loop
#THIS IS A LOOP IN ALOOP
#Run the following for better onderstanding
nums =[1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num,letter)
#Range function allows you to specify the number of iterations to conduct in a loop
#Example
for i in range(10):
    print(i)
#It displays the values 0,1,2,3,4,5,6,7,8,9
for i in range(1,11):#This specifies the range it prints from 1 upto 10.it doesn<t consider the last value
    print(i)
#8 While loop
#iterate until a certain condition is met
#you canuse break to break out of a while loop

#We can use the foor lop to carry out calculations in a list
#The for loop is used to carry out the power of every value in the list
#We can multiply a list by a scalar or add one list to another thus forming one big list
mylist = [1,2,3,4,5]
for x in mylist:
    print (pow(x,2))
    
#Sample code for calculating factorial
def multiply(*numbers):
  total = 1
  for number in numbers:
      total*= number
  return total

print(multiply(2,3,4,5))


x=0
while x < 10:
   print(x)
   x += 1
#The above results will be 0,1,2,3,4,5,6,7,8,9

#Infinite loop
x=0
while True:
   if x == 10:
       break
print(x)
x+=1
#if you remove the break fuction it will iterate infinitely
#ctrl + c can be used to terminate the infinite loop
