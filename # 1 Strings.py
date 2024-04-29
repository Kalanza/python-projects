#Working with textual data
message = "Hello World"
print(message)
#Message acts as a variable which stores the data "Hello world" and displays it.
#if your strings contains double quotes then you should use single quotes to enclose it.
#for example print("i'm only human")
#len used to find no of characters in the string
#example
print((len(message)))
#iT PRINTS THE NO 11 WHICH IS THE LENGTH OF THE STRING
#iF YOU WANT TO PRINT A CERTAIN LETTER OF THE WORD YOU CAN USE AN INDEX
print(message[3])
#It prints the letter L which occupies the third index.
print(message[0:3])
#This prints all the index from the first index upto the third index but it does not display the third index.
#In this it displays the letters Hel
print(message.upper())
#it onverts all the letters to uppercase
#It displays the letters HELLO WORLD
#message.lower()coverts all the words to lowercase
print(message.count('l'))
#It counts and returns the number of occurences of the string.
#It returns 3 which is the number of time l occurs in the word Hello World
print(message.find('World'))
#It displays 6 which is the first index of the word world
message= message.replace("World","Univerese")#This shows the new value of message
print(message)
#The replace function is used when you want to change a certain set of strings
#In this case we replace the word world with universe
greeting="Hello"
new = "Michael"
#It displays the message Hello, Michael
message = "{}, {}. welcome!".format(greeting, new)
print(message)
#it displlays the following Hello, Michael. welcome!
message = f"{greeting}, {new.upper()}. welcome!"
print(message)
#f String method is a better method of formating the strings as you are able to key in your dstacin curly 
#brackets
#It returns Hello, MICHAEL. welcome!
greeting="Hello"
new = "Michael"
print(dir(new))
#dir()it shows as all the attributes and methods that we have access to with that variable
print(help(str))
#it helps us to understand more about a certain dataype
print(help(str.lower))
