 The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
Write a sorting_hat.py program that asks the user some questions using int() and places them into one of the Houses based on their answers:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the house with the most points! 
  
def main():
    # Initialize house points
    gryffindor_points = 0
    ravenclaw_points = 0
    hufflepuff_points = 0
    slytherin_points = 0
    
    

    # Question 1
    print("Q1) Do you like Dawn or Dusk?")
    print("   1) Dawn")
    print("   2) Dusk")
    answer1 = int(input("Enter your choice (1 or 2): "))

    if answer1 == 1:
        gryffindor_points += 1
        ravenclaw_points += 1
    elif answer1 == 2:
        hufflepuff_points += 1
        slytherin_points += 1
    else:
        print("Wrong input.")

    # Question 2
    print("\nQ2) When I’m dead, I want people to remember me as:")
    print("   1) The Good")
    print("   2) The Great")
    print("   3) The Wise")
    print("   4) The Bold")
    answer2 = int(input("Enter your choice (1, 2, 3, or 4): "))

    if answer2 == 1:
        hufflepuff_points += 2
    elif answer2 == 2:
        slytherin_points += 2
    elif answer2 == 3:
        ravenclaw_points += 2
    elif answer2 == 4:
        gryffindor_points += 2
    else:
        print("Wrong input.")

    # Question 3
    print("\nQ3) Which kind of instrument most pleases your ear?")
    print("   1) The violin")
    print("   2) The trumpet")
    print("   3) The piano")
    print("   4) The drum")
    answer3 = int(input("Enter your choice (1, 2, 3, or 4): "))

    if answer3 == 1:
        slytherin_points += 4
    elif answer3 == 2:
        hufflepuff_points += 4
    elif answer3 == 3:
        ravenclaw_points += 4
    elif answer3 == 4:
        gryffindor_points += 4
    else:
        print("Wrong input.")

    # Determine the winning house
    houses = {
        "Gryffindor": gryffindor_points,
        "Ravenclaw": ravenclaw_points,
        "Hufflepuff": hufflepuff_points,
        "Slytherin": slytherin_points
    }
    winner = max(houses, key=houses.get)
    print(f"\nCongratulations! You belong to {winner}!")

if __name__ == "__main__":
    main()
