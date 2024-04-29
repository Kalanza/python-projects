total_candies = int(input("Enter the number of candies:"))
def to_smash(total_candies):

 if total_candies == 1:
    print("Splitting 1 candy")
 else:
    print("Splitting", total_candies, "candies")
#Here's a slightly more succinct solution using a conditional expression:

#print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

to_smash(91)
to_smash(1)