from random import randint as dice
input("Welcome to the dice rolling simulator! As the title suggests, this program simulates rolling a\n"
      "dice, and tells you the result. Press enter to roll the dice!\n")
answer = 0
i = 1
while answer == 0:
    if (i == 1):
        result = dice(1,6)
        print("The dice landed on:",result,"\n")
    again = input("Would you like to run the simulator again? Type yes or no:\n")
    if again == "yes" or again == "Yes":
        i = 1
        continue
    elif again == "no" or again == "No":
        break
    else:
        print("You must have entered something besides yes or no. Prompting for retry again.\n")
        i = 2
print("Thank you for using the dice simulator! The program will now terminate.")
