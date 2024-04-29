#Comparisons
#Object Identity: is
#if,if,else, prints the condition which is true 
#elif - it is used to check multiple staments
#it does not have switch case
#we can also use the following boolean operators
# and - returns true if both conditions are true
# or - returns true if either condition is true
# ,not - returns true if condition is false and vice versa
language = 'java'
if language == 'Java':
   print("Language is Java")
   print("Language is python") 
   print("No match")   
    
    #it will print language is Javasince  condtion 1 is correct
user = 'admin'
logged_in = "victor"
if user == "admin" and logged_in =="victor":
   print("The condition is true")
else:
 print("Condition is false")
    #in the code above if you use logical and it will display the message condition is true
    #if you use logical not it will display the message"condition is false.
    # object identity: checks if two entities have the same id
    #we use print(id()) to check the id of variables
    #Bolleans only return a value if it is true