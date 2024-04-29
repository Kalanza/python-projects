#Fizz_buzz algorithm
#Write a code such that if the number which is input is divisble by 3 it displays the word fizz
#if it is divisible by 5 it displays the word buzz
#If it is divisible by both 3 and 5 it displays the word fizzbuzz
#If it is divisible by none it displays the number
def fizz_buzz(x):
     if (x % 3 == 0) and (x % 5 == 0) :
        return "fizzbuzz"
     if x % 3 == 0 :
        return "fizz"
     if x % 5 == 0 :
        return "buzz" 
      
     return x
    
print(fizz_buzz(7))