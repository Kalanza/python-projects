#Lists - allows us to work with a list of values
#Lists are mutable-They can be modified
courses = ['history','Physics','Computer science']
print(courses)
#We can access a list by use of an index ie
print(courses[1])
#it returns 'pyhysics which occupies index 1
#list slicing-used to acces a couple of data
#append -it appends(adds) one value at the end of a list (it does no work with a tuple)
#example x.append(6) the new list will be [1, 2, 3, 4, 5, 6]
#insert -it appends(adds) one value at a specific index in a list and you have to specify the index
#example x.insert(4,"HEY") adds the value "Hey" at the fourth index
#remove -it removes a specific value in a list
#example x.remove(5) removes the value 5 from the list thus our new value will be [1, 2, 3, 4]
#pop - it allows you to remove a certain value in a specific index
#example x.pop(0) removes the value at index 0 which is 1 thus our new list will be [2, 3, 4, 5]
#index method - it returns the index of the value
# example x.index(3)
#print(x.index(3)) it displays the value 2 whose index position is 3
#sort method - it sorts our lists from smallest to largest
#extendother for example
#sorted function only returns a sortted version of that list without altering the original
#Sequences and collections
#We can access a specific type of data by use of slice
#example mylist[1:3]it will display data upto the third index but it won't display the third data
#it will display 20 and 30
#When accessing data from left to write we use the negative sign(-) and counting starts from -1
#mylist[-2] will display the string king
#we can also change data in the list 
#example mylist[3] = "Kalanza"
#the new value will be kalanza
#We can't append data in a tuple.It means we can"t add an additional value/index
mylist = [10,20,30,"victor","King",10.5]
print(mylist)

courses = ['History','Math','Geography','Chemistry']
courses_2 =['Physics','Businnes studies']
courses.extend(courses_2)
#it adds the two lists and the new values are
#['History', 'Math', 'Geography', 'Chemistry', 'Physics', 'Businnes studies']
print(courses)
x = [1,2,3,4,5]
x.index(3)
print(x.index(3))
#it returns 2 which is the index of  the value 3
#min,maxand sum
#it performs simple arithmetic functions in a list 
#Example
print(min(x))
#It returns 1 which is the minimum value in the list
print(max(x))
#It returns 5 which is the max value in the list
print(sum(x))
#it returns 15 which is the sum of the values in the list
#In fuction is used to check if a certain variable is in a lsit
print(1 in x)
#It returns true 1 is found in the list x
#In fuction is useful in loops such as for loop
#E xample
for num in (x):
    print(num)
#It returns the all the numbers  since it loops through five numbers
#we can usethe enumerate function to not only get the numbers but also the index of values in the list.
for index,num in enumerate (x):
    print(index,num)
#0 1
#1 2
#2 3
#3 4
#4 5
#Join function is used to convert a list into strings
courses = ['History','Math','Geography','Chemistry']
course_new = ' , '.join(courses)
print(course_new)
#it displays the values as strings separated by commas as we specified
#example it displays the following values History , Math , Geography , Chemistry
#WE can also convert the string to a list
#We use the split function
new_list = course_new.split(' , ')
print(new_list)
#it nows reverts back to list form
#Our new values are ['History', 'Math', 'Geography', 'Chemistry']
#Tuples,sets.Tuples are immutable-They can't be modified.
#Sets are values that are unordered and have no duplicates.
#They are used to get rid of duplicates and test if a value is a member of a set
#They determine which values they share or not.
#Example
new_courses = {'History','Math','Physics','CompSci'}
newer_course ={'History','Math','Art','Design'}
print(new_courses.intersection(newer_course))
#This functions serves to show similarity between the two set
#It returns {'Math', 'History'} which is common in both sets
#If you eplace intersection with difference it  will show you the values that are dissimilar
print(new_courses.difference(newer_course))
#it returns the values {'Physics', 'CompSci'}which are only found in new_courses
#Union is used to combine the two sets
print(new_courses.union(newer_course))
#it returns the combination of the two sets which is {'CompSci', 'Design', 'Physics', 'History', 'Math', 'Art'}
#Empty Lists
empty_list = []
empty_list= list()
#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()
#Empty Sets 
empty_set =  {} #This isn't right it is a dict
empty_set = set()
