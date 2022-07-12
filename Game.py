import random


rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")



scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

Game_gestures = [rock,paper,scissors]


user_choice = int(input("what do you choose type 0 for stone 1 for paper and 2 for scissors"))




computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice<0:
 print("its an invalid number")

else:
  
 print(Game_gestures[user_choice])

 print(Game_gestures[computer_choice])


if user_choice == computer_choice:
 print("It's A Draw !")


if user_choice == 1 and computer_choice == 0:
 print("You Won !")


if user_choice == 0 and computer_choice == 2:
 print("You Won !")

if user_choice == 2 and computer_choice == 0:
 print("You Lost !")


if user_choice == 2 and computer_choice == 1:
 print("You Won !")

  
elif user_choice == 1 and computer_choice == 2:
 print("you lost")



elif user_choice == 0 and computer_choice == 1:
 print("you lost")


elif user_choice == 1 and computer_choice == 2:
 print("you lost")
